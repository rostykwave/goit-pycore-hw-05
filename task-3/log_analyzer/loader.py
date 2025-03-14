from typing import List, Dict
from log_analyzer.parser import parse_log_line

def load_logs(file_path: str) -> List[Dict[str ,str]]:

    try:
        with open(file_path, "r", encoding="utf-8") as file:
           return [parse_log_line(line) for line in file if parse_log_line(line)]
        # Альтернативний спосіб:
        #  return list(filter(lambda log: log, map(parse_log_line, file)))
        ## filter(lambda log: log, ...) відкидає порожні значення ({}).
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)