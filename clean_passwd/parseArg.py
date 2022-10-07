#!/usr/bin/python3

import sys
import deluser

server = []
user = []

def read_args():
    args_length = len(sys.argv)
    print("Number of arguments are:",args_length)
    x = 0
    while x < args_length - 1:
        s = sys.argv[x+1].split(":")[0]
        u = sys.argv[x+1].split(":")[1]
#        print("server is:", s, "user is:", u)
        x = x + 1
        server.append(s)
        user.append(u)


def main():
    read_args()
    z = 0
    while z < len(server):
        print("Remove:",user[z],"from:",server[z])
        z = z + 1
    confirm = input('Are you sure? (Y/N)')
    if confirm == "Y":
        y = 0
        while y < len(server):
            if not deluser.check_file_exist(server[y]):
                print("passwd file", server[y], " doesn't exist, please check.")
            elif not deluser.check_user(server[y], user[y]):
                print("User", user[y], "does not exists in", server[y])
            else:
                print("checking out file", server[y])
                deluser.checkout(server[y])
                print("Removing", user[y], "from", server[y])
                deluser.remove_user(server[y], user[y])
                print("checking in file", server[y])
                deluser.checkin(user[y], server[y])
            y = y + 1
    else:
        print("Abort")


if __name__ == "__main__":
    main()
