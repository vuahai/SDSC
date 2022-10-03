#!/usr/bin/python3
import sys

# Check for 2 inputs
def check_args():
    if len(sys.argv) == 3:
        print ("It's TRUE")
        return 1
    else:
        print ("It's FALSE")

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
#    user = sys.argv[2]
#    passfile = sys.argv[1]
    if check_args() == 1:
        remove_user(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
