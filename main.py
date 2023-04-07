# imports
import os
import platform
import random
import time

# info

name = "PyShell"
if os.path.exists("version"):
    with open("version", "r") as f:
        version = f.read().strip()
else:
    print("ERR: version file not found. Could not run PyShell.")
    exit()
banner = """                           
█▀█ █▄█ █▀ █░█ █▀▀ █░░ █░░
█▀▀ ░█░ ▄█ █▀█ ██▄ █▄▄ █▄▄
"""

if os.path.exists("username.txt") and os.path.exists("password.txt"):
    with open("username.txt", "r") as f:
        username = f.read().strip()
    with open("password.txt", "r") as f:
        password = f.read().strip()
    print(f"Welcome, {username}! Please enter your password.")
    password_verify = input("> ")
    if password_verify == password:
        print("Successfully logged in!")
    else:
        print("Invalid password.")
        exit()
else:
    print("Welcome! Please create your username.")
    username = input("> ")
    if len(username) < 4 or len(username) > 24:
        print("Username can't be shorter than 4 and longer than 24.")
        exit()
    else:
        with open("username.txt", "w") as f:
            f.write(username)
        print(f"Good choice, {username}! Now please create your password.")
        password = input("> ")
        if len(password) < 4 and len(password) < 24:
            print("Password can't be shorter than 4 and longer than 24.")
            exit()
        else:
            print("Successfully signed up!")
            with open("password.txt", "w") as f:
                f.write(password)

if platform.system() == "win32":
    os.system("cls")
else:
    os.system("clear")
print(f"Welcome to {name} {version}!")

while True:
    try:
        cmd = input(f"{username}@{name}~#$ ")

        if cmd  == "" or cmd == " " or cmd == "  " or cmd == "   " or cmd == "     ":
            continue
        elif cmd == "help" or cmd == "Help":
            print("Full list of commands:")
            print("Help - Shows this command")
            print(f"Exit - Exits {name}")
            print("Clear - Clears the console")
            print("Whoami - Tells you your user")
            print("Echo - Says something")
            print("Fetch - Fetches the data about PyShell (and if you're on Linux it prints some data about the system.)")
            print("Coinflip - Flips a coin")
            print("os.{command} - Does a system command")
        elif cmd == "exit" or cmd == "Exit":
            exit()
        elif cmd == "clear" or cmd == "Clear":
            if platform.system() == "win32":
                os.system("cls")
            else:
                os.system("clear")
        elif cmd == "whoami" or cmd == "Whoami":
            print(username)
        elif cmd.startswith("echo") or cmd.startswith("Echo"):
            echo = cmd[4:].strip()
            print(echo)
        elif cmd == "fetch" or cmd == "Fetch":
            if platform.system() == "Linux":
                print(banner)
                print(f"Name: {name}")
                print(f"Version: {version}")
                os.system('echo Distro: $(sed -n \'s/^PRETTY_NAME="//p\' /etc/os-release | cut -f1 -d\'"\')')
                os.system('echo Linux username: $(whoami)')
                os.system('echo Hostname: $(hostname)')
                os.system('echo Uptime: $(uptime -p | sed "s/up //")')
            else:
                print(banner)
                print(f"Name: {name}")
                print(f"Version: {version}")
        elif cmd == "flip" or cmd == "Flip":
            flips = ["Heads", "Tails"]

            print(random.choice(flips))

        elif cmd.startswith("os.") or cmd.startswith("Os."):
            os.cmd = cmd[3:].strip()
            os.system(os.cmd)

        else:
            print(f"ERR: Command {cmd} not found.")
    except KeyboardInterrupt:
        continue