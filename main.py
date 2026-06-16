from parser.parser import parser
from detection.rules import detect

def main():
    #Parses all the logs into a list format.
    logs = parser()

    for log in logs:
        detect(log)


if __name__ == "__main__":
    main()