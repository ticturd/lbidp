from parser.parser import parser
from detection.rules import detect_bruteforce, detect_user_enumeration


def detect(logs):
    for log in logs:
        ip = log["IP"]
        message = log["Message"].lower() #Make the message lowercase to make it easier for detection in rules.
        debug_bf = detect_bruteforce(ip, message)
        debug_ue = detect_user_enumeration(ip, message)

        if debug_bf or debug_ue == "STOP":
            print("Stopped.")
            return
    




def main():
    #Parses all the logs into a list format.
    logs = parser()

    
    detect(logs)


if __name__ == "__main__":
    main()