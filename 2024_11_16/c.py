n, k = map(int, input().split())
s = input()

s_find = lambda ch, idx: s.find(ch, idx)

one_idx = []
zero_idx = []
i = 0
while (i < n):
    if (s[i] == '1'):
        one_idx.append(i)
        i = s_find('0', i + 1)
    else:
        i = s_find('1', i + 1)
    if (len(one_idx) >= k):
        break

def f(idx): # k-1番目の1の塊の最後のiを返す
    x = s_find('0', idx)
    if (x > 0):
        return x - 1
    return n - 1

result = s[:f(one_idx[k-2])+1]
# print(0, f(one_idx[k-2])+1) #debug
result += s[one_idx[k-1]:f(one_idx[k-1])+1]
# print(one_idx[k-1], f(one_idx[k-1])+1) #debug
result += s[f(one_idx[k-2])+1:one_idx[k-1]]
# print(f(one_idx[k-2])+1, one_idx[k-1]) #debug
result += s[f(one_idx[k-1])+1:]
# print(f(one_idx[k-1])+1, n) #debug
print(result)
