from sys import argv
from os import getcwd
from json import dumps, loads
import pathlib as pt
import subprocess as sp

home = pt.Path.home()
USER_DATA_PATH = f"{home}/.directory_book.json"
ASF_TARGET_PATH = "/tmp/asf_target"
CWD = getcwd()


def read_user_data() -> dict:
    try:
        with open(USER_DATA_PATH, "r") as f:
            txt = f.readline()
            return loads(txt)

    # Previous configuration not found or unreadable. Starting a new directory book.
    except Exception:
        return {}


def write_user_data(data: dict):
    try:
        with open(USER_DATA_PATH, "w+") as f:
            txt = dumps(data)
            f.write(txt)

    except Exception as err:
        print("Failed to save user data.", err)


def write_target(target: str):
    try:
        with open(ASF_TARGET_PATH, "w+") as f:
            f.write(target + "\n")

    except Exception as err:
        print("Failed to save target.", err)


def print_help():
    help_msg = """ASF
    Usage:
        <name> adds the current directory to the list using the <name> alias. Overwrites if existing.
        --help (-h) display this message
        --list (-l) to list known directories
        --remove (-r) <name> remove the corresponding directory from the list.
        --fzf (-f) navigate using fzf
        --list-fzf (-lf) list directories in a fzf friendly way.
    """
    print(help_msg)


#! TODO dot command (add pwd as the dir name)
dir_book = read_user_data()
cli_args = argv[1:]


if not cli_args:
    print_help()
    exit(1)

cmd = cli_args[0]

# Help
if cmd == "-h" or cmd == "--help":
    print_help()
    exit(1)

# List
if cmd == "-l" or cmd == "--list":
    print("Current mapped directories:")
    for el in dir_book:
        print(f"\t- {el}: {dir_book[el]}")
    exit(1)

# List (fzf friendly)
if cmd == "-lf" or cmd == "--list-fzf":
    for el in dir_book:
        print(f"{el}")
    exit(1)

# Navigate with Fzf
if cmd == "-f" or cmd == "--fzf":
    keys = " \n ".join(dir_book.keys())
    choice = sp.check_output(f"echo '{keys}' | fzf", shell=True, encoding="utf8")
    clean = choice.strip()
    write_target(dir_book[clean])
    exit()

# Remove
if cmd == "-r" or cmd == "--remove":
    try:
        key = cli_args[1]
    except KeyError:
        print("Missing key to remove. Eg. asf -r my-repo")
        exit(1)

    dir_book.pop(key, None)
    write_user_data(dir_book)
    exit(1)

jump_target = cmd

if jump_target in dir_book:
    target = dir_book[jump_target]
    write_target(target)
    exit()

else:
    dir_book[jump_target] = CWD
    write_user_data(dir_book)
    print(f"Name {jump_target} set to {CWD}")
    exit(1)
