[cert, n, uncert, rank] = list(map(int, input().split()))

if (rank <= cert):
    print(1.0)
elif (rank <= n):
    print(uncert / (n - cert))
else :
    print(0.0)
