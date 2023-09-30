t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().strip().split()))[:n]
    #converting list into set,so that it contain only unique values
    a=set(l)
    print(len(a))
    t=t-1
