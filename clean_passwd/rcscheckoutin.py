#!/usr/bin/python3

import subprocess
import sys

pwfile = sys.argv[2]

def checkout(file):
    subprocess.run(["co","-l",file])

def checkin(user2delete, file):
    message = "deleted", user2delete
    msg_arg = "-m", " ".join(message)
    arg = "".join(msg_arg)
    subprocess.run(["ci","-u",arg,file])

if sys.argv[1] == "out":
    checkout(pwfile)
elif sys.argv[1] == "in":
    checkin(sys.argv[3],pwfile)
else:
    exit(0)