#List of universal sensitive users. Main one to look out for universally is root, other ones are there just to showcase. Not using regex as OpenSSH logs are highly predictable.
sensitive_users = ["root", "admin", "administrator", "sysadmin", "oracle", "postgres", "mysql", "backup", "operator"]


def get_username(message):
    parts = message.split()     #Splitting message into parts so i can identify keywords in the log line for the username.

    if "invalid user" in message:
        return parts[parts.index("user") + 1]

    elif "for" in parts:
        return parts[parts.index("for") + 1]
        
    elif "user" in parts:
        return parts[parts.index("user") + 1]
        
    else:
        return None


alerts = []

def create_alert(rule, severity, ip, username, message):
    alerts.append(
        {"rule" : rule,
         "severity" : severity,
         "ip" : ip,
         "username" : username,
         "message" : message
         }
    )
    
    



