import subprocess

# Check if there are changes
status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)

if not status.stdout.strip():
    print("Nothing to commit. Working tree clean.")
else:
    message = input("Enter commit message: ").strip()

    if not message:
        print("Commit aborted. No message provided.")
    else:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        subprocess.run(["git", "push"])
        print("Changes pushed to GitHub successfully.")
