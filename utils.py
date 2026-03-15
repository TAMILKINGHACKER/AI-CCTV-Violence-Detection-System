import os
import time

def ensure_folders():
    os.makedirs("evidence", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def log_event(message):
    ensure_folders()
    with open("logs/incidents.log","a") as f:
        f.write(f"{time.ctime()} - {message}\n")
