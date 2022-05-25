#!/usr/bin/env python3

import sys
import re

rgb_in = sys.stdin.readline()
rgb = re.findall("\d*", rgb_in)
hexcol = ""
for color in rgb:
	if color:
		hexcol += hex(int(color))[2:].zfill(2)
print("#" + hexcol)
