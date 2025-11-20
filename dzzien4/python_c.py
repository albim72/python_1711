import subprocess

result = subprocess.run(["./program"], capture_output=True, text=True)
print(result.stdout)

with open("program/mymodule.c", "r", encoding="utf-8") as f:
    code = f.read()

print(code)
