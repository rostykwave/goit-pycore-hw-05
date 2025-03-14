from typing import Dict, List

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    log_count = {}
    for log in logs:
        level = log["level"]
        log_count[level] = log_count.get(level, 0) + 1
    
    return log_count