n, q = map(int, input().split())
hand = { 'L':1, 'R':2 }

def ope(h, t):
    p_cnt = 0
    left = hand['L']
    right = hand['R']
    if (h == 'R'):
        if (right == t):
            return p_cnt
        if (right > left and left > t):
            return t + n - right
        if (t > left and left > right):
            return right + n - t
        return abs(t - right)
    # h = 'L'
    if (left == t):
        return p_cnt
    if (left > right and right > t):
        return t + n - left
    if (t > right and right > left):
        return left + n - t
    return abs(t - left)

cnt = 0
for i in range(q):
    h, t = input().split()
    cnt += ope(h, int(t))
    hand[h] = int(t)
print(cnt)
