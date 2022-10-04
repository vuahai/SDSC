#!/usr/bin/python3
import re
import sys

s = sys.argv[2]
pwfile = sys.argv[1]
out = None
with open(pwfile) as file:
    for line in file:
        if re.search(r'\b' + line.split(":")[0] + r'\b', s):
            out = "found"
            print('{0} found'.format(line))
    if out is None:
        print(s,"not found")
