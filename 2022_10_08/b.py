n, m = map(int, input().split())

k = []
x = []
for i in range(m):
    row = list(map(int, input().split()))
    k.append(row[0])
    x.append(row[1:])

pair = {}
for i in range(1, n + 1):  # 1 ~ n
    pair[i] = []
for i in range(m):  # 舞踏会ごと
    for j in range(k[i]):  # 一人ごとに見てる
        pair[x[i][j]] += x[i]

# print(pair)
num = []
for i in range(1, n + 1):
    num.append(i)
result = "Yes"
for i in range(1, n + 1):
    if(set(pair[i]) != set(num)):
        result = "No"
print(result)
