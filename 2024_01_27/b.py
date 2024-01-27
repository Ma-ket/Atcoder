s = list(input())
s = sorted(s)
sc = list(sorted(set(s)))
count = 0
c = []
for i in range(len(sc)):
    for st in s:
        if sc[i] == st:
            count += 1
    c.append(count)
    count = 0
m = max(c)
for i in range(len(c)):
    if m == c[i]:
        print(sc[i])
        break


# めも: set()はソートされた状態では返ってこない。ソートした状態で渡しても、意図した順序で返ってこない泣
