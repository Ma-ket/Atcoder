# 入力
a, b = map(int, input().split())

if(a > b):
    tmp = a
    a = b
    b = tmp

if(a == b):
    print(a)
elif(a == 0):
    print(b)
elif((a == 1 and b == 2) or (a == 1 and b == 3) or (a == 2 and b == 3)):
    print(3)
elif((a == 1 and b == 4) or (a == 1 and b == 5) or (a == 4 and b == 5)):
    print(5)
elif((a == 2 and b == 4) or (a == 2 and b == 6) or (a == 4 and b == 6)):
    print(6)
else:
    print(7)

