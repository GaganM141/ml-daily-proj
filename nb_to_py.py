import subprocess

subprocess.run([
    "jupyter", "nbconvert",
    "--to", "script",
    "Untitled.ipynb"
])
