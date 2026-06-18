from parser.parser import parser

failed_attempts = {}
flagged_ips = {}
invalid_users = {}

#Thresholds for flagging will be able to be changed by the user later. Right now it is just hard coded for testing purposes.

#Note: Message is converted to lowercase in main.
def detect_bruteforce(ip, message):
    if "failed password" not in message:
        return

    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1    #If IP exists, adds 1 to its current count. Otherwise it starts from 1

    if failed_attempts[ip] >= 5 and flagged_ips.get(ip) != "bruteforce":
        flagged_ips[ip] = "bruteforce"
        print(f"Bruteforce detected from IP: {ip}")
        return "STOP"

def detect_user_enumeration(ip, message):
    if "invalid user" not in message:
        return
    
    invalid_users[ip] = invalid_users.get(ip, 0) + 1    #^^^

    if invalid_users[ip] >= 3 and flagged_ips.get(ip) != "user_enumeration":
        flagged_ips[ip] = "user_enumeration"
        print(f"User enumeration detected from IP: {ip}")
        return "STOP"
