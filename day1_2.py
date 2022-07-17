import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

tot = 0
i = 0
for c in lines[0]:
    tot += 1 if (c == "(") else -1
    i += 1
    if tot == -1:
        print(i)
        exit()

# 4 min