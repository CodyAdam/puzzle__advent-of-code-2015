lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = [[0] * 1000 for _ in range(1000)]

for line in lines:
    left, right = line.split(" through ")
    command = left.split(" ")

    x1, y1 = [int(x) for x in command[-1].split(',')]
    x2, y2 = [int(x) for x in right.split(',')]
    command = " ".join(command[0:-1])

    for x in range(x1, x2 + 1, 1 if x2 - x1 >= 0 else -1):
        for y in range(y1, y2 + 1, 1 if y2 - y1 >= 0 else -1):
            if command == "turn on":
                grid[y][x] = 1
            elif command == "turn off":
                grid[y][x] = 0
            else:
                grid[y][x] = 1 if not grid[y][x] else 0

count = 0
for row in grid:
    count += sum(row)
print(count)

# 15 min
