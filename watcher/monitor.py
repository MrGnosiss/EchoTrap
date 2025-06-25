# watcher/monitor.py
import time, os, json
from watcher.alert import send_alert
from utils.logger import log_event

with open('config.json') as f:
    config = json.load(f)

def start_monitoring():
    tracked_files = [f"{config['canary_dir']}/{f}" for f in os.listdir(config['canary_dir'])]
    last_states = {f: os.path.getmtime(f) for f in tracked_files}

    while True:
        for f in tracked_files:
            try:
                current = os.path.getmtime(f)
                if current != last_states[f]:
                    log_event(f"⚠️ Canary triggered: {f}")
                    send_alert(f)
                    last_states[f] = current
            except FileNotFoundError:
                continue
        time.sleep(2)
