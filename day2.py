lines = [line.strip() for line in open("input.txt", 'r').readlines()]


def surface(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


surf = []
for line in lines:
    l, w, h = [int(x) for x in line.split("x")]
    surf.append(surface(l, w, h) + min([l * w, w * h, l * h]))

print(sum(surf))

# 4min
