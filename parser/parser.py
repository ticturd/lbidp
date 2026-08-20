import os   #Using this for file path stuff

def get_log_file():
    
    demo_log_files = sorted(os.listdir("data/demo_logs"))

    for index, file in enumerate(demo_log_files):
        print(f"{index + 1}. {file}")

    while True:
        try:
            chosen_file = int(input())
            if chosen_file in range(1, len(demo_log_files) + 1):
                used_file = demo_log_files[chosen_file - 1]
                return os.path.join("data/demo_logs", used_file)
            else:
                print("Choice out of range.")
        except ValueError:
            print("Incorrect value. Please enter a valid integer.")


    


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

#Can't remember why I'm getting this, might have later refined this in rules.py but I'm not sure.
def get_event_type(line):
    before, sep, after = line.partition(" - ")    #Separator must be " - " with spaces in order to avoid confusing it with other dashes in the log line.
    if sep == " - ":
        event_type = after.strip()
        return event_type
    else:
        return "N/A"


def get_ip(parts):
    for part in parts:
        #Will probably change later. For now we just check if the part has 3 dots in it, which follows the format of a typical IP address.
        if part.count(".") == 3:
            return part    
    return "N/A"

def parser(file_path):
    raw_logs = []   
    with open(file_path, "r") as file:
        for line in file:
            raw_logs.append(line.strip())


    parsed_logs = []
    try: 
        for log in raw_logs:           
            parts = log.split() #For timestamp and source

            ip = get_ip(parts)
            if ip == "N/A":
                continue

            timestamp = get_timestamp(parts)
            source = get_source(parts)
            event_type = get_event_type(log)
            message = get_message(log)


            parsed_logs.append({"IP":ip,"Timestamp":timestamp, "Source":source, "Message":message, "Event Type":event_type})
    
    except Exception as error:
        message = f"Log parsing failed: sample logs may be malformed. Error: {str(error)}"
        print(message)
        return message

    return parsed_logs

