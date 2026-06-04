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


def get_message(first_line):
    before, sep, after = first_line.partition(":")
    message = after.strip()

    return message


def main():
    raw_logs = get_raw_logs()

    #First line (test)
    for line in raw_logs:
        first_line = line
        break
    parts = first_line.split() #For timestamp and source

    #Main
    timestamp = get_timestamp(parts)
    source = get_source(parts)
    message = get_message(first_line)

    print(f"Time: {timestamp}")
    print(f"Source: {source}")
    print(f"Message: {message}")
    return

main()