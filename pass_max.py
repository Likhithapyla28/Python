T=int(input())
while(T):
    N,X=map(int,input().split())
    A=list(map(int,input().strip().split()))[:N]
    A.sort(reverse=True)
    print(A[X-1]-1)
    T=T-1
