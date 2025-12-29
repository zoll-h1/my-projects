import subprocess
import sys

def run_command(cmd: list):
    subprocess.run(cmd, check=True)
if len(sys.argv) < 2:
    print("Message: please provide a commit message.")
    print("Usage: python manager.py <commit_message>")
    sys.exit(1) 
message = sys.argv[1]
print("Starts working...")
run_command(["git", "add", "."])
run_command(["git", "commit", "-m", message])
print("Ready to push changes.")

