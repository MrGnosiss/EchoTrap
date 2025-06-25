# echotrap.py
from watcher.deploy import deploy_canaries
from watcher.monitor import start_monitoring
from utils.logger import banner

if __name__ == "__main__":
    banner()
    deploy_canaries()
    start_monitoring()
