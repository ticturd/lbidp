def get_raw_logs():
    #Reads sample logs, appends every line to a raw log list.
    raw_logs = []

    with open("data/sample_logs.log", "r") as logs:
        for _ in logs:
            line = _.strip()
            raw_logs.append(line)

    return raw_logs


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


def get_message(line, event_type):
    uncleaned_message = line.split(":", 2)[-1].strip() #This is doing 3 operations at once. In short, it just splits the line into three parts: timestamp and source, the middle parts, actual message.

    if uncleaned_message.endswith(event_type):
        cleaned_message = uncleaned_message[:-len(event_type)]
        cleaned_message = cleaned_message.replace(" - ", "")
        return cleaned_message.strip()
    else:
        return uncleaned_message


def get_event_type(line):
    #Separator must be " - " with spaces in order to avoid confusing it with other dashes in the log line.
    before, sep, after = line.partition(" - ")
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

def parser():
    raw_logs = get_raw_logs()

    parsed_logs = []
    try: 
        for _ in raw_logs:
            line = _
            
            parts = line.split() #For timestamp and source

            ip = get_ip(parts)
            timestamp = get_timestamp(parts)
            source = get_source(parts)
            event_type = get_event_type(line)
            message = get_message(line, event_type)


            parsed_logs.append({"IP":ip,"Timestamp":timestamp, "Source":source, "Message":message, "Event Type":event_type})
    
    except Exception as error:
        message = f"Log parsing failed: sample logs may be malformed. Error: {str(error)}"
        print(message)
        return message

    return parsed_logs

