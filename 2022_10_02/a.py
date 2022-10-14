# n, m, x = 1000, 25, -1
def main():
    res = []
    for num in range(1, 10):
        cnt, mod = 1, num % m
        while (cnt <= n):
            if (mod == 0):
                cnt = n // cnt * cnt
                break
            cnt += 1
            mod = (mod * 10 + num) % m
        else:
            cnt, num = -1, -1
        res.append((cnt, num))
    cnt, ans = sorted(res)[-1]
    if (cnt != -1):
        print(str(ans) * cnt)
    else:
        print(-1)
    return

if (__name__ == '__main__'):
    n, m = map(int, input().split())

    main()
