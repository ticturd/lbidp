from parser.parser import get_log_file, parser
from detection.rules import init_ip_flag, detect_bruteforce, detect_user_enumeration, detect_sensitive_user_login, detect_break_in
from detection.utilities import alerts


def detect(logs):
    for log in logs:
        ip = log["IP"]
        message = log["Message"].lower() #Make the message lowercase to make it easier for detection module, as having uppercase letters complicates things.
        
        init_ip_flag(ip)
        detect_bruteforce(ip, message)
        detect_user_enumeration(ip, message)
        detect_sensitive_user_login(ip, message)
        detect_break_in(ip, message)

        

def main():
    #Parses all the logs into a list format, then runs the detection.
    log_file = get_log_file()
    print(log_file)
    logs = parser(log_file)
    detect(logs)

    

if __name__ == "__main__":
    main()