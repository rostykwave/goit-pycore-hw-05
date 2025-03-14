import sys
from log_analyzer.loader import load_logs

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)


if __name__ == "__main__":
    main()