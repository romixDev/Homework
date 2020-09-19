now = -1
max = 0
prevMax = 0
while now != 0:
    now = int(input())
    if now >= max:
        prevMax = max
        max = now
    if max > now > prevMax:
        prevMax = now
print(prevMax)
