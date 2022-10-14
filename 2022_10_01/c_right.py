
N=int(input())
A=list(map(int,input().split()))
L=[0]*(N+1)
sell_book=0
for i in range(N):
    if(A[i]<=N):
        if(L[A[i]]==0):
            L[A[i]]=1
        else:
            sell_book+=1
    else:
        sell_book+=1
#print(sell_book,L)
for i in range(1,N+1):
    if(L[i]==1):
        N-=1
    else:
        N-=2
    if(N==0):
        print(i)
        exit()
    elif(N<0):
        print(i-1)
        exit()
print(N)
