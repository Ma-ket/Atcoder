key = list(input())
tap = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

cnt = 0
pos = 0
for c in tap:
    idx = key.index(c)
    cnt += abs(pos - idx)
    if (idx == 25):
        break
    pos = idx
print(cnt)
