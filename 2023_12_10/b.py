k, g, m = map(int, input().split())

i, gra, mag = 0, 0, 0
while (i < k):
    if (gra == g):
        gra = 0
    elif (mag == 0):
        mag = m
    else:
        tmp = gra + mag
        if (tmp <= g):
            gra = tmp
            mag = 0
        elif(tmp > g):
            gra = g
            mag = tmp - g
    i += 1
print(f"{gra} {mag}")
