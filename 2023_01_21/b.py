n = int(input())
s = list(input())

start = 0
while(start <= n):
    string = "".join(s)
    index = string.find('na', start)
    if(index == -1):
        break
    s.insert(index + 1, 'y')
    # print(index, start)
    start = index + 2
    n += 1
print("".join(s))
