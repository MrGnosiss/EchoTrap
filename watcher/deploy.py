# watcher/deploy.py
import shutil
import os
import json

with open('config.json') as f:
    config = json.load(f)

def deploy_canaries():
    dest = config['canary_dir']
    os.makedirs(dest, exist_ok=True)
    canary_templates = ['invoice.pdf', 'creds.txt']
    for cfile in canary_templates:
        if not os.path.exists(f"{dest}/{cfile}"):
            shutil.copyfile(f"canaries/{cfile}", f"{dest}/{cfile}")
