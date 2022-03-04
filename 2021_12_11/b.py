count = int(input())
point = 0
name = ""
dic = {name : point}

while True:
    point = 0
    if(count == 0):
        break
    count -= 1

    name =input()
    if(name in dic):
        dic[name] += 1
    else:
        point = 1
        dic[name] = point

max = 0
a = ""
for key in dic:
    if(max < dic[key]):
        max = dic[key]
        a = key

print(a)


