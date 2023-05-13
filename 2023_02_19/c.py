n, k = map(int, input().split())
a = list(map(int, input().split()))

def Mex(seq):
    for i in range(k + 1):
        if (i not in seq):
            return i

mex_max = 0
# 最初に全探索でbの数列を全て作る
b_seq = []
# 先頭のindexを指定
for first in range(n - k + 1):
    # 最後尾のindexを指定
    for end in range(first + k - 1, n):



print(mex_max)
