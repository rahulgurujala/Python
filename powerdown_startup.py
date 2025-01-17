# Script Name		: powerdown_startup.py
# Author                : Craig Richards
# Created		: 05th January 2012
# Last Modified		: 21th September 2017
# Version		 : 1.0

# Modifications		:

# Description		: This goes through the server list and pings the machine, if it's up it will load the putty session, if its not it will notify you.

import os  # Load the Library Module
import subprocess  # Load the Library Module
from time import strftime  # Load just the strftime Module from Time


def windows():  # This is the function to run if it detects the OS is windows.
    f = open("server_startup_" + strftime("%Y-%m-%d") + ".log", "a")  # Open the logfile
    for server in open(
        "startup_list.txt", "r"
    ):  # Read the list of servers from the list
        ret = subprocess.call(
            f"ping -n 3 {server}",
            shell=True,
            stdout=open("NUL", "w"),
            stderr=subprocess.STDOUT,
        )

        if ret == 0:  # If you get a response.
            f.write(f"{server.strip()}: is alive, loading PuTTY session" + "\n")
            subprocess.Popen(f"putty -load {server}")
        else:
            f.write(f"{server.strip()} : did not respond" + "\n")


def linux():
    f = open("server_startup_" + strftime("%Y-%m-%d") + ".log", "a")  # Open the logfile
    for server in open("startup_list.txt"):  # Read the list of servers from the list
        ret = subprocess.call(
            f"ping -c 3 {server}",
            shell=True,
            stdout=open("/dev/null", "w"),
            stderr=subprocess.STDOUT,
        )

        if ret == 0:  # If you get a response.
            f.write(f"{server.strip()}: is alive" + "\n")
            subprocess.Popen(["ssh", server.strip()])
        else:
            f.write(f"{server.strip()}: did not respond" + "\n")


# End of the functions

# Start of the Main Program

if os.name == "posix":  # If the OS is linux...
    linux()  # Call the linux function
elif os.name in ("nt", "dos", "ce"):  # If the OS is Windows...
    windows()  # Call the windows function
else:
    print("Not supported")
