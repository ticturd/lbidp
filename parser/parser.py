#Log file is now selected in ui.py

def get_timestamp(parts):
    timestamp_tokens = [parts[0], parts[1], parts[2]]

    #Components are separated by a space
    timestamp = " ".join(timestamp_tokens)

    return timestamp


def get_source(parts):
    for part in parts:
        if part.endswith(":"):
            source = part.strip(":")
            return source


def get_message(line):
    message = line.split(":", 2)[-1].strip()  #This is doing 3 operations at once. In short, it just splits the line into three parts: timestamp and source, the middle parts, actual message.
    return message

#get_event_type removed, as it is irrelevant for the program.


def get_ip(parts):
    for part in parts:
        #Will probably change later. For now we just check if the part has 3 dots in it, which follows the format of a typical IP address.
        if part.count(".") == 3:
            return part    
    return "N/A"

def parser(file_path):
    parsed_logs = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                log = line.strip()
                parts = log.split() #For timestamp and source

                ip = get_ip(parts)
                if ip == "N/A":
                    continue

                timestamp = get_timestamp(parts)
                source = get_source(parts)
                message = get_message(log)

                parsed_logs.append({"IP" : ip, "Timestamp" : timestamp, "Source": source, "Message" : message})

    except Exception as error:
        message = f"Log parsing failed: sample logs may be malformed. Error: {str(error)}"
        print(message)
        return []

    return parsed_logs

