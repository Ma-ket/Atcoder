n = int(input())
s = list(input())

if (set(s[:n//2]) == set('1')
        and set(s[n//2+1:]) == set('2')
        and len(set(s[:n//2])) == len(set(s[n//2+1:]))
        and s[n//2] == '/'):
    print(('Yes'))
else:
    print('No')
