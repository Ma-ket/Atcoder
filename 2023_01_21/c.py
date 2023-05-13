n, a, b = map(int, input().split())
s = list(input())

s += s
cost = 1 << 60  # 適当に大きい数字
for i in range(n):
    tmp = a * i  # n回回せば元の文字列に戻るため全探索
    for j in range(n // 2):  # 半分の量を回してみる
        if(s[i + j] != s[i + n - 1 - j]):  #
            tmp += b
    cost = min(tmp, cost)
print(cost)
