import sys
import math

while True:
    start_line = sys.stdin.readline().split()
    if start_line:
        r = float(start_line[0])
        print(r-1)
    else:
        break
