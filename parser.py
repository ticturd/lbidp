def get_raw_logs():
#Reads sample logs, appends every line to a raw log list.
    raw_logs = []

    with open("sample_logs.log", "r") as logs:
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
    before, sep, after = line.rpartition(":")

    #The message is the part after the last colon, but we need to remove the event type from it if it exists.
    uncleaned_message = after.strip()

    if uncleaned_message.endswith(event_type):
        cleaned_message = uncleaned_message[:-len(event_type)].strip()
        return cleaned_message
    else:
        return uncleaned_message


def get_event_type(line):

    before, sep, after = line.partition("-")
    if sep == "-":
        event_type = after.strip()
        return event_type
    else:
        return


def parser():
    raw_logs = get_raw_logs()

    parsed_logs = []

    for _ in raw_logs:
        line = _
        
        parts = line.split() #For timestamp and source

        timestamp = get_timestamp(parts)
        source = get_source(parts)
        event_type = get_event_type(line)
        message = get_message(line, event_type)


        parsed_logs.append({"Timestamp":timestamp, "Source":source, "Message":message, "Event Type":event_type})


    for logs in parsed_logs:
        for key, value in logs.items():
            print(f"{key}: {value}")
        print("\n")


    return parsed_logs

def main():
    parser()


if __name__ == "__main__":
    main()