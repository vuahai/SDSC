#!/usr/bin/python3
import sys
import os.path
import re
import subprocess


# Check for 2 inputs
def check_args():
    if len(sys.argv) == 3:
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
        return True
    else:
        return False

# Check to see if user exists
def check_user(pwfile, user):
    out = None
    with open(pwfile) as file:
        for line in file:
            if re.search(r'\b' + line.split(":")[0] + r'\b', user):
#                out = "notNone"
                return True
        if out is None:
#            print(user,"not found")
            return False

# Check to see if passwd file exists and if user to be deleted exists
def remove_user(pwfile, user):
     with open(pwfile) as file:
        for line in file:
            if line.split(":")[0] != user:
                f = open(r"passwd_tmp","a")
                f.write(line)
        os.replace('passwd_tmp',pwfile)
#                 new_file(line)

#def remove_user(pwfile, user):
#    with open(pwfile) as input:
#        with open(temp_file, "w") as output:
#            for line in input:
#                line = line.replace(user, "")
#            output.write(line)
#    os.replace('temp_file',pwfile)

# Create new file
#def new_file(line):
#    f = open(r"passwd.new", "a")
#    f.write(line)

def checkout(file):
    subprocess.run(["co","-l",file])

def checkin(user2delete, file):
    message = "deleted", user2delete
    msg_arg = "-m", " ".join(message)
    arg = "".join(msg_arg)
    subprocess.run(["ci","-u",arg,file])

def main():
    if not check_args():
        print ("Usage: clean_pass.py [passwd_file] [username]")
    elif not check_file_exist(passwdFile):
        print("passwd file",passwdFile," doesn't exist, please check.")
    elif not check_user(passwdFile, user2delete):
        print("User",user2delete,"does not exists in",passwdFile)
    else:
        print("checking out file", passwdFile)
        checkout(passwdFile)
        print("Removing", user2delete, "from", passwdFile)
        remove_user(passwdFile, user2delete)
        print("checking in file", passwdFile)
        checkin(user2delete, passwdFile)

if __name__ == "__main__":
    main()

