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

        

def analyse(log_file):
    p_log_file = parser(log_file)    
    detect(p_log_file)

    return alerts
    
