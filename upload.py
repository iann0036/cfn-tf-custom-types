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


resourcedir = Path("resources") / sys.argv[1].split("::")[1].lower() / sys.argv[1].replace("::","-")
shutil.copyfile("cloudformation-cli-python-lib-0.0.1.tar.gz", (resourcedir / "cloudformation-cli-python-lib-0.0.1.tar.gz").absolute())
shutil.copyfile("terraform", (resourcedir / "src" / sys.argv[1].replace("::","_").lower() / "terraform").absolute())
os.chmod((resourcedir / "src" / sys.argv[1].replace("::","_").lower() / "terraform").absolute(), 0o777)

check_call(['cfn', 'submit', '--set-default'], resourcedir.absolute())

os.remove((resourcedir / "cloudformation-cli-python-lib-0.0.1.tar.gz").absolute())
os.remove((resourcedir / "src" / sys.argv[1].replace("::","_").lower() / "terraform").absolute())
shutil.rmtree((resourcedir / "build").absolute())

