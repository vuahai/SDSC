#!/usr/bin/python3
import re
import sys

s = 'tnguyen'
pwfile = sys.argv[1]
with open(pwfile) as file:
    for line in file:
        if re.search(r'\b' + line.split(":")[0] + r'\b', s):
            print('{0} found'.format(line))
