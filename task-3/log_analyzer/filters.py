from typing import List, Dict

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log["level"].upper() == level.upper()]