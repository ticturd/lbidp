from parser.parser import parser
from detection.rules import detect_bruteforce, detect_user_enumeration


def detect(log):
    ip = log["IP"]
    message = log["Message"].lower() #Make the message lowercase to make it easier for detection in rules.
    detect_bruteforce(ip, message)
    detect_user_enumeration(ip, message)






def main():
    #Parses all the logs into a list format.
    logs = parser()

    for log in logs:
        detect(log)


if __name__ == "__main__":
    main()