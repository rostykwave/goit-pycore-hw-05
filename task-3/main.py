import sys
from log_analyzer.loader import load_logs
from log_analyzer.filters import filter_logs_by_level
from log_analyzer.statistics import count_logs_by_level, display_log_counts, display_filtered_logs

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            display_filtered_logs(filtered_logs, log_level)
        else:
            print(f"\nNo records found for level '{log_level.upper()}'.")


if __name__ == "__main__":
    main()