from detection.utilities import sensitive_users, get_username, create_alert

failed_attempts = {}
ip_flags = {} 
invalid_users = {}

#Each function generates an alert, with rule broken, severity etc. for user interface.

#Thresholds for flagging will be able to be changed by the user later. Right now it is just hard coded for testing purposes.

#Initialises a list for the flagged ip, so reasons can be added. 
def init_ip_flag(ip):
    if ip not in ip_flags:  
        ip_flags[ip] = []


#Note: Message is converted to lowercase in main.
def detect_bruteforce(ip, message):    
    if "failed password" not in message:
        return

    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1    #If IP exists, adds 1 to its current count. Otherwise it starts from 1

    if failed_attempts[ip] >= 5 and "bruteforce" not in ip_flags[ip]:  
        ip_flags[ip].append("bruteforce")  

        username = get_username(message)
        create_alert("bruteforce", "high", ip, username, message)
        print(f"Bruteforce detected from IP: {ip}")


def detect_user_enumeration(ip, message):
    if "invalid user" not in message:
        return
    
    invalid_users[ip] = invalid_users.get(ip, 0) + 1    #If IP exists, adds 1 to its current count. Otherwise it starts from 1

    if invalid_users[ip] >= 3 and "user_enumeration" not in ip_flags[ip]:  
        ip_flags[ip].append("user_enumeration")  
        
        username = get_username(message)
        create_alert("user_enumeration", "medium", ip, username, message)
        print(f"User enumeration detected from IP: {ip}")


def detect_sensitive_user_login(ip, message):
    # Only act on successful logins, accepted publickey is becoming more prevalent than passwords.
    if "accepted password" not in message and "accepted publickey" not in message:
        return
    
    # No username = nothing to check
    username = get_username(message)
    if username is None:
        return

    # Sensitive user login
    if username in sensitive_users and "sensitive_user_login" not in ip_flags[ip]:  
        ip_flags[ip].append("sensitive_user_login")  
        create_alert("sensitive_user_login", "high", ip, username, message)
        print(f"Sensitive user login detected from IP {ip} for {username}")

def detect_break_in(ip, message):
    # Only act on successful logins, accepted publickey is becoming more prevalent than passwords.
    if "accepted password" not in message and "accepted publickey" not in message:
        return

    # No username = nothing to check
    username = get_username(message)
    if username is None:
        return

    # Login after bruteforce
    if "bruteforce" in ip_flags[ip] and "break_in" not in ip_flags[ip]:  
        ip_flags[ip].append("break_in")  
        create_alert("break_in", "critical", ip, username, message)
        print(f"Break in attempt detected from IP {ip} and Username {username}")