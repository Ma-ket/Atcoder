n = int(input())
a = list(map(int, input().split()))

def rule1():
    for i in range(0, len(a)-1):  # i = 0->n-1
        d = a[i] - a[i+1]
        if(abs(d) > 1):
            return i
    return -1

def rule2(i):
    d = a[i] - a[i+1]
    if(d > 1):  # a[i]の方が大きい
        a.insert(i+1, a[i]-1)
    elif(d < -1):  # a[i]の方が小さい
        a.insert(i+1, a[i]+1)

def main():
    while(True):
        rule = rule1()
        if(rule == -1):
            print(*a)
            break
        else:
            rule2(rule)

main()
