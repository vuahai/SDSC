#!/usr/bin/python3
import sys
import os.path
import re

# Check for 2 inputs
def check_args():
    if len(sys.argv) == 3:
        print ("It's TRUE")
        global passwdFile
        passwdFile = sys.argv[1]
        global user2delete
        user2delete = sys.argv[2]
        return True
    else:
        return False

# Check to see if passwd file exists
def check_file_exist(file):
    if True == os.path.exists(file):
        print("File Exists")
        return True
    else:
        return False

def remove_user(pwfile, user):
    out = None
    with open(pwfile) as file:
        for line in file:
            if re.search(r'\b' + line.split(":")[0] + r'\b', user):
                out = "notNone"
        if out is None:
            print(user,"not found")
        else:
            with open(pwfile) as file:
                for line in file:
                    if line.split(":")[0] != user:
                        new_file(line)
# Create new file
def new_file(line):
    f = open(r"passwd.new", "a")
    f.write(line)

def main():
    if not check_args():
        print ("Usage: clean_pass.py [passwd_file] [username]")
    elif not check_file_exist(passwdFile):
        print("passwd file",passwdFile," doesn't exist, please check.")
    else:
        print("2 args and passwd file exists")
        remove_user(passwdFile, user2delete)

if __name__ == "__main__":
    main()
