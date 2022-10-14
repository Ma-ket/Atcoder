n, q = map(int, input().split())

l = [0]

for _ in range(n):
    l.append(list(map(int, input().split())))

st = []

for _ in range(q):
    st.append(list(map(int, input().split())))

def func(t, row):
    return row[t]

for i in range(q):
    s, t = st[i]

    print(func(t, l[s]))
