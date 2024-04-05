from sys import argv
from os import getcwd, environ
from json import dumps, loads
import pathlib as pt


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


#! TODO dot command (add pwd as the dir name)
dir_book = read_user_data()
cli_args = argv[1:]

if not cli_args:
	print("""
	ASF
	Usage:
	 <name> adds the current directory to the list using the <name> alias. Overwrites if existing.
	 -l to list known directories
	 -r <name> remove the corresponding directory from the list.

	""")
	exit(1)

cmd = cli_args[0]

# List
if cmd == "-l" or cmd == "--list":
	print("Current mapped directories:")
	for el in dir_book:
		print(f"\t- {el}: {dir_book[el]}")
	exit(1)

# Remove
if cmd == "-r" or cmd == "--remove":
	try:
		key = cli_args[1]
	except KeyError:
		print("Missing key to remove. Eg. asf -r nyrepo")
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


