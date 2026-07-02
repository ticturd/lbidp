from parser.parser import parser
from detection.rules import init_ip_flag, detect_bruteforce, detect_user_enumeration, detect_break_in

def detect(logs):
    for log in logs:
        ip = log["IP"]
        message = log["Message"].lower() #Make the message lowercase to make it easier for detection in rules.
        
        init_ip_flag(ip)
        detect_bruteforce(ip, message)
        detect_user_enumeration(ip, message)
        detect_break_in(ip, message)

        

def main():
    #Parses all the logs into a list format.
    logs = parser()
    detect(logs)


if __name__ == "__main__":
    main()