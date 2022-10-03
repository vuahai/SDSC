#!/usr/bin/python3
import sys
import os.path

# Check to see if passwd file exists
def check_file_exist():
    if True == os.path.exists(sys.argv[1]):
        print("File Exists")
        return True
    else:
        return False

# Check for 2 inputs
def check_args():
    if len(sys.argv) == 3:
        print ("It's TRUE")
        return True
    else:
        return False

# Output of file san user
def remove_user(passwdfile, user): 
    with open(passwdfile) as file:
        for line in file:
            if line.split(":")[0] != user:
#                new_file(line.rstrip("\n"))
                new_file(line)

# Create new file
def new_file(line):
    f = open(r"passwd.new", "a")
    f.write(line)

def main():
    if not check_args():
        print ("Usage: clean_pass.py [passwd_file] [username]")
    elif not check_file_exist():
        print("passwd file",sys.argv[1]," doesn't exist, please check.")
    else:
        print("2 args and passwd file exists")
        remove_user(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
