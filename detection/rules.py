from parser.parser import parser
from detection.utilities import sensitive_users, get_username

failed_attempts = {}
flagged_ips = {}
invalid_users = {}

#Thresholds for flagging will be able to be changed by the user later. Right now it is just hard coded for testing purposes.

#Initialises a list for the flagged ip, so reasons can be added. 
def init_ip_flag(ip):
    if ip not in flagged_ips:
        flagged_ips[ip] = []


#Note: Message is converted to lowercase in main.
def detect_bruteforce(ip, message):    
    if "failed password" not in message:
        return

    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1    #If IP exists, adds 1 to its current count. Otherwise it starts from 1

    if failed_attempts[ip] >= 5 and "bruteforce" not in flagged_ips[ip]:
        flagged_ips[ip].append("bruteforce")
        print(f"Bruteforce detected from IP: {ip}")


def detect_user_enumeration(ip, message):
    if "invalid user" not in message:
        return
    
    invalid_users[ip] = invalid_users.get(ip, 0) + 1    #^^^

    if invalid_users[ip] >= 3 and "user_enumeration" not in flagged_ips[ip]:
        flagged_ips[ip].append("user_enumeration")
        print(f"User enumeration detected from IP: {ip}")


def detect_break_in(ip, message):
    # Only act on successful logins
    if "accepted password" not in message:
        return

    # No username = nothing to check
    username = get_username(message)
    if username is None:
        return

    # Sensitive user login
    if username in sensitive_users and "break_in" not in flagged_ips[ip]:
        flagged_ips[ip].append("break_in")
        print(f"Break in from IP {ip} and Username {username}")

    # Login after bruteforce
    elif "bruteforce" in flagged_ips[ip] and "break_in" not in flagged_ips[ip]:
        flagged_ips[ip].append("break_in")
        print(f"Break in detected from IP {ip} and Username {username}")
    