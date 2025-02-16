#!/usr/bin/python3


# 1. Add argparse
# this should read a prefix for the python binary created



# 2. Create a virtual env in the current directory called venv


# 3. Create the {prefix}-python script
# This script should have some setopts
# script_dir is the directory that contains the executable
# This runs exec $script_dir/env/bin/python3 "$*"
# Use """ string


# 4. Create {prefix}-pip like the {prefix} python script
# but this runs pip in the virtual env


import argparse
import os
import stat
import subprocess
import sys

parser = argparse.ArgumentParser(description="Create a python binary with a specified prefix")
parser.add_argument("prefix", help="Prefix for the python binary")
args = parser.parse_args()

def main():

    python_file = f"{args.prefix}-python"
    pip_file = f"{args.prefix}-pip"


    existing_files = [x for x in ["env", python_file, pip_file] if os.path.exists(x)]

    if existing_files:
        print(f"{existing_files} exists")
        sys.exit(1)


    subprocess.check_call(["python3", "-m", "venv", "env"])

    script_content = """
    #!/bin/bash
    set -e
    script_dir="$(dirname "$(readlink -f "$0")")"
    exec "$script_dir/env/bin/python3" "$@"
    """
    with open(python_file, "w") as f:
        f.write(script_content)

    # 4. Create {prefix}-pip like the {prefix} python script
    pip_script_content = """
    #!/bin/bash
    set -e
    script_dir="$(dirname "$(readlink -f "$0")")"
    exec "$script_dir/env/bin/pip" "$@"
    """
    with open(pip_file, "w") as f:
        f.write(pip_script_content)

    # Make python python and pip executable
    # only add the executable flag
    make_executable(python_file)
    make_executable(pip_file)

def make_executable(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)

if __name__ == "__main__":
    main()
