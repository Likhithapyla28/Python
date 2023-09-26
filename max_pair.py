# cook your dish here
t=int(input())
while(t):
    N,M=map(int,input().split())
    l=list(map(int,input().strip().split()))[:N]
    l.sort(reverse=True)
    su=0
    c=0
    for i in range(N):
        su=su+l[i]
        if(su>=M):
            print(i+1)
            c=1 
            break
         
    if(c==0):
        print("-1")
        
        
    t=t-1
    
        
        
        
