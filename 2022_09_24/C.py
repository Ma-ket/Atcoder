# 解答見てる

import sys
sys.setrecursionlimit(10 ** 8)
# 入力
n, x, y = map(int, input().split())

# 辞書さ作成
tree = {}

# 辞書の中にリストを作成
for i in range(1, n + 1):
    tree[i] = []
for i in range(1, n):
    # 入力
    s, e = map(int, input().split())
    # start
    tree[s].append(e)
    # end
    tree[e].append(s)

# [False, False, ... , False, False]
visited = [False] * (n + 1)
path = [x]

# start, end
def dfs(pos, des):
    if (pos == des):
        return True
    # # 引用
    # > # start
    # > tree[s].append(e)
    # > # end
    # > tree[e].append(s)
    for npos in tree[pos]:
        if (visited[npos] == False):
            visited[npos] = True
            path.append(npos)
            state = dfs(npos, des)
            if (state == True):
                return True
            path.pop()
            visited[npos] = False

    return False

visited[x] = True
dfs(x, y)
ret = [str(i) for i in path]
print(" ".join(ret))
