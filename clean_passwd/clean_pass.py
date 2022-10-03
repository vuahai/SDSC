#!/usr/local/python3

import sys

user = sys.argv[2]
with open(sys.argv[1]) as file:
    for line in file:
        if line.find(user) != 0:
            print(line.rstrip())
