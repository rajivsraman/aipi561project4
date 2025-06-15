import json
from datetime import datetime

LOG_PATH = "usage_log.jsonl"

def log_usage(prompt, user, response):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "user": user,
        "prompt": prompt,
        "response_len": len(response),
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")