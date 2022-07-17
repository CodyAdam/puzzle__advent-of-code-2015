import hashlib

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

key = "ckczppom"

i = 0
out = hashlib.md5((key + str(i)).encode()).hexdigest()
while out[:5] != "00000":
    i += 1
    out = hashlib.md5((key + str(i)).encode()).hexdigest()

print(i)

# 7 min
