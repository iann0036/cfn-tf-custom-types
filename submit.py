import shutil
import sys
import subprocess
import os
from pathlib import Path


def check_call(args, cwd):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        print(stderr)
        raise subprocess.CalledProcessError(
            returncode=proc.returncode,
            cmd=args)
    
    return stdout


print("Preparing package...")
resourcedir = Path("resources") / sys.argv[1].split("::")[1].lower() / sys.argv[1].replace("::","-")

print("Submitting...")
check_call(['cfn', 'submit', '--set-default'], resourcedir.absolute())

print("Cleaning up...")
shutil.rmtree((resourcedir / "build").absolute())
