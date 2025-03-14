from typing import List, Dict
from log_analyzer.parser import parse_log_line

def load_logs(file_path: str) -> List[Dict[str ,str]]:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parse_log_line(line) for line in file if parse_log_line(line)]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)
    
    return logs