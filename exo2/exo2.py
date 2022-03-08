#!/usr/bin/env python3
import re

file = open("./exo2.txt", 'r')
a = re.findall("main : {\n(?:.* = .*\n)*}", file.read())
print(a)