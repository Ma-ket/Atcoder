import numpy

def cost(a, b, c, d):
    return numpy.sqrt((a-c)**2 + (b-d)**2)

n = int(input())
sm_list = []
a = 0
b = 0
for i in range(n):
    c, d = map(int, input().split())
    sm_list.append(cost(a, b, c, d))
    a = c
    b = d
sm_list.append(cost(a, b, 0, 0))

print(sum(sm_list))
