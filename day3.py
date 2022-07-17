lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = {}
grid = dict()
x = 0
y = 0


def mark(x, y):
    if (x, y) in grid:
        grid[(x, y)] += 1
    else:
        grid[(x, y)] = 1


mark(x, y)
for c in lines[0]:
    if c == ">":
        x += 1
    if c == "<":
        x -= 1
    if c == "^":
        y += 1
    if c == "v":
        y -= 1
    mark(x, y)

print(len(grid))

# 4 min
