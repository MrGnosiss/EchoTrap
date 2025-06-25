# utils/logger.py
import datetime

def log_event(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("trap.log", "a") as f:
        f.write(f"{timestamp} {message}\n")
    print(f"{timestamp} {message}")

def banner():
    print(r"""
 _____ _               _             
| ____| | ___  ___  __| | ___ _ __   
|  _| | |/ _ \/ _ \/ _` |/ _ \ '_ \  
| |___| |  __/  __/ (_| |  __/ | | | 
|_____|_|\___|\___|\__,_|\___|_| |_| 
[+] EchoTrap - Canary Alert System by Mr. Axolotl
    """)
