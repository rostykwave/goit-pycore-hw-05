from typing import Dict, List

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    log_count = {}
    for log in logs:
        level = log["level"]
        log_count[level] = log_count.get(level, 0) + 1
    
    return log_count
# Альтернативний спосіб:
#   return reduce(lambda acc, log: {**acc, log["level"]: acc.get(log["level"], 0) + 1}, logs, {})

def display_log_counts(counts: Dict[str, int]):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level.ljust(16)} | {counts.get(level, 0)}")

def display_filtered_logs(logs: List[Dict[str, str]], level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")