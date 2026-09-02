from parser.parser import parser
from detection.rules import init_ip_flag, detect_bruteforce, detect_user_enumeration, detect_sensitive_user_login, detect_break_in



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

    if not p_log_file:
        return None # Return None if parsing failed

    detect(p_log_file)

    
