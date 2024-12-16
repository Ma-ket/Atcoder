s = input()

a = []
i = 0
while (i < len(s)):
    if ('|' == s[i]):
        idx = s.find('|', i + 1)
        if (idx < 0):
            break
        a.append(idx - i - 1)
        i = idx
    else:
        i += 1
print(*a)
