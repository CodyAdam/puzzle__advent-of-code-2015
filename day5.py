import hashlib

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

vowels = set(["a", "e", "i", "o", "u"])
dont = set(["ab", "cd", "pq", "xy"])

count = 0
for string in lines:
    has_2_same = False
    vowels_count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            vowels_count += 1
        if i < len(string) - 1 and string[i + 1] == string[i]:
            has_2_same = True
    has_invalid = False
    for no in dont:
        if no in string:
            has_invalid = True
    if not has_invalid and has_2_same and vowels_count >= 3:
        count += 1

print(count)

# 8 min
