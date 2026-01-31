import subprocess
from datetime import datetime

message = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", message])
subprocess.run(["git", "push"])
