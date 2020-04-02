#!/usr/bin/env python3

################################################################################
## Simple python3 script to create a Component.jsx and Component.module.scss  ##
## inside the usual ./src/components/Component folder                         ##
################################################################################


from pathlib import Path, PurePath
import argparse
from argparse import RawTextHelpFormatter

description = """
Create a new React Component Folder with files.
By default the first letter of the component will be capitalized and a Sass module
and a package.json will be created.
-
Example: mkrcp Component
This will create Component.jsx, Component.module.scss and a package.json inside ./src/components/Component
-
"""

parser = argparse.ArgumentParser(
    description=description, formatter_class=RawTextHelpFormatter
)

# Positional arguments
parser.add_argument("component", help="name of the new react component")

# Optional arguments
parser.add_argument(
    "-c", "--css", help="create a css module stylesheet", action="store_true"
)
parser.add_argument(
    "-s",
    "--scss",
    help="create a scss module stylesheet - this is the default and therefore not required",
    action="store_true",
)
parser.add_argument(
    "-ns", "--nostyle", help="no stylesheet module will be created", action="store_true"
)
parser.add_argument(
    "-nj", "--nojson", help="no package.json will be created", action="store_true"
)
parser.add_argument(
    "-l",
    "--lower",
    help="do not capitalize the first letter of the component",
    action="store_true",
)
parser.add_argument(
    "-p",
    "--path",
    help="path where the new component will be created - if not specified it will be ./src/components/",
)
parser.add_argument("-q", "--quiet", help="do not print output", action="store_true")


args = parser.parse_args()

component = args.component
style_extension = ".scss"  # defalut stylesheet type
output = ""

if not args.lower:
    component = component.capitalize()

if args.path:
    path = PurePath(args.path).joinpath(component)
else:
    path = PurePath(Path.cwd()).joinpath("src/components/" + component)

if args.css:
    style_extension = ".css"

if args.scss:
    style_extension = ".scss"

if args.nostyle:
    style_extension = False

# Create directory
Path(path).mkdir(mode=0o755, parents=True, exist_ok=True)
# Create jsx file
Path(PurePath(path).joinpath(component + ".jsx")).touch(mode=0o644, exist_ok=True)
output = f"{component}.jsx created inside {path}"
# Create style module
if style_extension:
    Path(PurePath(path).joinpath(component + ".module" + style_extension)).touch(
        mode=0o644, exist_ok=True
    )
    output += f"\n{component}{style_extension} created inside {path}"
# Create package.json file
if not args.nojson:
    Path(PurePath(path).joinpath("package.json")).write_text(
        "{\n\t" + f'"main": "{component}.jsx"' + "\n}"
    )
    output += f"\npackage.json created inside {path}"

if not args.quiet:
    print(output)
