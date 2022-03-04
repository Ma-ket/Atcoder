N, Q = map(int, input().split())
tall = list(map(int, input().split()))

for _ in range(Q):
    x = int(input())
    point = 0
    for height in tall:
        if(x <= height):
            point += 1
    print(point)