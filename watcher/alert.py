# watcher/alert.py
import json
import smtplib
from email.mime.text import MIMEText
from utils.logger import log_event

with open('config.json') as f:
    config = json.load(f)

def send_alert(file_path):
    message = f"EchoTrap Alert: Canary file accessed - {file_path}"
    log_event(message)
    # You can later add real SMTP creds here if needed
    print(f"[EchoTrap] ALERT: {message}")
