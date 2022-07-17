import hashlib

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

vowels = set(["a", "e", "i", "o", "u"])
dont = set(["ab", "cd", "pq", "xy"])

count = 0
for string in lines:
    has_split = False
    has_2_duo = False
    for i in range(len(string) - 2):
        if string[i + 2] == string[i]:
            has_split = True
    for i in range(len(string) - 1):
        for j in range(len(string) - 1):
            if string[i:i + 2] == string[j:j +
                                         2] and j != i and abs(i - j) >= 2:
                has_2_duo = True
                break
    if has_split and has_2_duo:
        count += 1

print(count)

# 17 min
