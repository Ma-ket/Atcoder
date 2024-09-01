n = int(input())
h = []
for i in range(n):
    h.append(list(map(int, input().split())))

def load_into_dump(d, dump, height, cost):
    dump += d
    height -= d
    cost += d
    return dump, height, cost

def unload(d, dump, height, cost):
    dump -= d
    height += d
    cost += d
    return dump, height, cost

def move(dump, cost):
    cost += 100 + dump
    return cost

