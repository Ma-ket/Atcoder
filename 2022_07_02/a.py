k = int(input())
hour = 21
minite = 0

while(k >= 60):
    k -= 60
    hour += 1

minite = k

if(minite < 10):
    print(hour, ":0", minite, sep='')
else:
    print(hour, ":", minite, sep='')
