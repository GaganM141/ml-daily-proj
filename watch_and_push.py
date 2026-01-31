from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess, time
from datetime import datetime

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".ipynb"):
            msg = f"Auto save update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["python", "nb_to_py.py"])
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", msg])
            subprocess.run(["git", "push"])

observer = Observer()
observer.schedule(Watcher(), ".", recursive=True)
observer.start()

print("Watching notebook changes... Press CTRL+C to stop")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
