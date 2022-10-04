#!/usr/bin/python3

import sys

server = []
user = []

def read_args():
    args_length = len(sys.argv)
    print("Number of arguments are:",args_length)
    x = 0
    while x < args_length - 1:
        s =  sys.argv[x+1].split(":")[0]
        u = sys.argv[x+1].split(":")[1]
        print("server is:",s,"user is:",u)
        x = x + 1
        server.append(s)
        user.append(u)

read_args()

print(server[2],user[2])
