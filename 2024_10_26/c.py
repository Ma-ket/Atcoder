n, m = map(int, input().split())
ab = []
for _ in range(m):
    ab.append(tuple(map(int, input().split())))

masu = {}
pab = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
cnt = 0
for a, b in ab:
    if ((a, b) not in masu.keys()):
        masu[(a, b)] = 1
        cnt += 1
    for pa, pb in pab:
        aa = a + pa
        bb = b + pb
        if (not(aa < 1 or aa > n or bb < 1 or bb > n)):
            if ((aa, bb) not in masu.keys()):
                cnt += 1
                masu[(aa, bb)] = 1

print(n**2 - cnt)
