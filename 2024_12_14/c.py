point = list(map(int, input().split()))

standings = []
for bit in range(1, 32):
    solved_point = 0
    name = ""
    for digit in range(5):
        # bit立っている桁目が解いた名前
        if bit & 1 << digit:
            solved_point += point[digit]
            name += "ABCDE"[digit]
        standing.append((solved_point, name))

# 要チェック
# https://atcoder.jp/contests/abc384/editorial/11611
