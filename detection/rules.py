from parser.parser import parser

failed_attempts = {}
flagged_ips = set() #Using set to prevent duplicate ips from being added, rather than a list.

def detect(log):
    ip = log["IP"]
    message = log["Message"]

    if "Failed password" in message:
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        if failed_attempts[ip] >= 5 and ip not in flagged_ips:
            print(f"ALERT: Brute force attack detected from port [{ip}]")
            flagged_ips.add(ip)

