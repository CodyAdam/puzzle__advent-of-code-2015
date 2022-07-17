lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = {}
x = 0  # santa pos
y = 0
x2 = 0  # robot santa pos
y2 = 0


def mark(x, y):
    if (x, y) in grid:
        grid[(x, y)] += 1
    else:
        grid[(x, y)] = 1


isSanta = True
mark(x, y)
mark(x2, y2)
for c in lines[0]:
    if isSanta:
        if c == ">":
            x += 1
        if c == "<":
            x -= 1
        if c == "^":
            y += 1
        if c == "v":
            y -= 1
        mark(x, y)
    else:
        if c == ">":
            x2 += 1
        if c == "<":
            x2 -= 1
        if c == "^":
            y2 += 1
        if c == "v":
            y2 -= 1

        mark(x2, y2)
    isSanta = not isSanta

print(len(grid))

# 8 min
