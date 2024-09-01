s = list(input())
s.append(" ")

ops = ("+", "-", "*", "/")
op = None
values = []
result = 0
for i in range(len(s)):
    if (s[i] in ops):
        op = s[i]
    else:

            break
print(result)
