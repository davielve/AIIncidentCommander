import time
import json
import random
import os
from datetime import datetime

LOG_DIR = "/data/logs"
SERVICES = ["api-gateway", "auth-service", "payments-service", "notification-service", "postgres-db"]
LEVELS = ["INFO", "WARN", "ERROR"]

os.makedirs(LOG_DIR, exist_ok=True)

def generate_log():
    service = random.choice(SERVICES)
    level = random.choices(LEVELS, weights=[0.8, 0.15, 0.05])[0]
    
    # Simulate a crisis if payments-service is picked
    message = "Request processed successfully"
    if service == "payments-service" and level == "ERROR":
        message = "Connection timeout to upstream payment provider"
    elif level == "ERROR":
        message = f"Unexpected exception occurred in {service}"
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "service": service,
        "level": level,
        "message": message
    }
    
    file_path = os.path.join(LOG_DIR, f"{service}.log")
    with open(file_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    print(f"Starting log generator, writing to {LOG_DIR}...")
    while True:
        generate_log()
        time.sleep(random.uniform(0.5, 2.0))
