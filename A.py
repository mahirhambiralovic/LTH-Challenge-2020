import sys

while True:
    start_line = sys.stdin.readline().split()
    if start_line:
        N = int(start_line[0])
        sum = 0
        for i in range(N):
            line = sys.stdin.readline().lower()
            if "rose" in line or "pink" in line:
                sum+=1
        if sum == 0:
            print("I must watch Star Wars with my daughter")
        else:
            print(sum)
    else:
        break
