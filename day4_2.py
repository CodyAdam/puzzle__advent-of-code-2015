import hashlib

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

key = "ckczppom"

i = 0
out = hashlib.md5((key + str(i)).encode()).hexdigest()
while out[:6] != "000000":
    i += 1
    out = hashlib.md5((key + str(i)).encode()).hexdigest()

print(i)

# 8 min
