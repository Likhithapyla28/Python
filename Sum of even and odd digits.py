#Your code goes here
N=int(input())
l=len(str(N))
osum=0
esum=0
while(N>0):
    r=N%10
    if(r%2==0):
        esum=esum+r
    else:
        osum=osum+r
    N=int(N/10)
print(esum,"\t",osum)



























