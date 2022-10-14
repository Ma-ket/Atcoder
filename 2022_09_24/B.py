x, y, z = map(int, input().split())

dist = 0

if (x > 0):
    if (y > 0 and x > y):
        if (z > 0 and y >= z):
            dist = x
        elif (z > 0 and y < z):
            dist = -1
        else:
            dist = abs(z) * 2 + x
    else:
        dist = x
else:
    if (y < 0 and x < y):
        if (z < 0 and z >= y):
            dist = abs(x)
        elif (z < 0 and z < y):
            dist = -1
        else:
            dist = z * 2 + abs(x)
    else:
        dist = abs(x)

print(dist)
