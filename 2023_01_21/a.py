n, p, q, r, s = list(map(int, input().split()))
a_list = list(map(int, input().split()))

b_list = a_list

pq = a_list[p - 1:q]
rs = a_list[r - 1:s]
# print(pq)
# print(rs)

b_list[p - 1:q] = rs
b_list[r - 1:s] = pq

print(*b_list)
