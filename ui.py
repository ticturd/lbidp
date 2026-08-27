from analyse import analyse
from detection.rules import reset_variables
import dearpygui.dearpygui as dpg
import os

#Utility for getting selected log file.
def begin_analysis():

    selected_log_file = dpg.get_value("selected_log_file")

    #No log file selected = empty string. 
    if selected_log_file != '':
        reset_variables()  # Reset variables before starting a new analysis
        log_file = os.path.join("data/demo_logs", selected_log_file)
        results = analyse(log_file)
        format_alerts(results)
    else:
        dpg.configure_item("error_text", show=True)
    


def format_alerts(alerts):
    formatted_alerts = []
    for alert in alerts:
        formatted_alert = (
            f"[{alert['severity']}] {alert['rule']}\n"
            f"IP: {alert['ip']}\n"
            f"Username: {alert['username']}\n"
            "-------------------------"
        )
        formatted_alerts.append(formatted_alert)

    dpg.set_value("analysis_results", "\n".join(formatted_alerts))


#Main UI function.
def run_ui():
    dpg.create_context()

    with dpg.window(label="Log Based Intrusion Detection Prototype", tag="main_window"):
        dpg.add_text("Welcome!")

        dpg.add_separator()
        dpg.add_text("Select a log file:")

        dpg.add_combo(
            items = os.listdir("data/demo_logs"),
            tag = "selected_log_file"
        )

        #Error text that will be displayed if the user tries to start analysis without selecting a log file.
        dpg.add_text(
            "Please select a log file above before starting.",
            color = (255, 0, 0),
            tag = "error_text",
            show = False
        )

        dpg.add_button(label="Analyse", callback=begin_analysis)

        dpg.add_separator()
        dpg.add_text("Results:")

        dpg.add_text(
            "Analysis results will be displayed here!",
            tag = "analysis_results"
        )

    dpg.create_viewport(title="LBIDP", width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main_window", True)

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

    dpg.destroy_context()


if __name__ == "__main__":
    run_ui()