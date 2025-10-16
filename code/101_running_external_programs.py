import subprocess
completed = subprocess.run(["ls","-l"])
print(completed.args)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)