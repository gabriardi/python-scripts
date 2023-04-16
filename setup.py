#!/usr/bin/env python3

################################################################################
## Setup: copy the scripts inside scripts folder to /usr/local/bin            ##
##        and make them executable                                            ##
################################################################################


from pathlib import Path, PurePath
from shutil import copyfile

from_folder = Path("./scripts")
to_folder = Path("~/.local/bin")
permissions = 0o755  # rwxrxrx

all_scripts = list(from_folder.glob("**/*.py"))
for script in all_scripts:
    destination_filename = PurePath(script).stem  # without .py extension
    destionation_fullpath = PurePath(to_folder).joinpath(destination_filename)
    copyfile(script, destionation_fullpath)
    # change file permissions to executable
    Path(destionation_fullpath).chmod(permissions)
    print(f"Added: {destionation_fullpath}")
