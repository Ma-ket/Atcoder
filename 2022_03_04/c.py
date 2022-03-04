(a, b) = (map(int, input().split()))

mn = b / 0.1
std = a / 0.08
mx = (b + 1) / 0.1

print(mn, std, mx)

if (mn <= std and std <= mx):
    print(int(std))
else :
    print(-1)
