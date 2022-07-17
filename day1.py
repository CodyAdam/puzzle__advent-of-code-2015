import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

tot = 0
for c in lines[0]:
    tot += 1 if (c == "(") else -1

print(tot)

# 1min50