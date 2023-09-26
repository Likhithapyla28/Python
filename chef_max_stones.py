# cook your dish here
t=int(input())
while(t):
    N=int(input())
    l=list(map(int,input().strip().split()))[:N]
    chef=0
    l.sort(reverse=True)
    for i in range(0,N,2):
        chef=chef+l[i]
    print(chef)
    t=t-1
