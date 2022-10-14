    # 正解

## 入力
n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)  # [0, 0, 0, ... , 0, 0]
sell_books = 0

for i in range(n):
    if (a[i] <= n):  # 読めない巻なのか
        if (l[a[i]] == 0):  # とりまチェック
            l[a[i]] = 1
        else:  # 被ってるじゃねーか
            sell_books += 1
    else:  # 読めないので売る
        sell_books += 1
# print(sell_book,L)

for i in range(1, n + 1):
    if (l[i] == 1):  # 読めるぞ
        n -= 1
    else:  # 読めん
        n -= 2

    if (n == 0):
        print(i)
        exit()
    elif (n < 0):
        print(i - 1)
        exit()

print(n)
