##import sys
##def solve():
##    da=iter(sys.stdin.read().split())
##    n=int(next(da)
##    
##if __name__=='__main__':
##    solve()


import sys
import bisect
def solve():
    da=iter(sys.stdin.read().split())
##    da=iter('''3 4
##2 5 1
##1 3
##2 2
##2 2
##2 2
##'''.split())
    n,m=int(next(da)),int(next(da))
    si=[int(next(da)) for _ in range(n)]
    s=[float('-inf')]+sorted(si)+[float('inf')]
    deff=[0]*(n+2)
    diff=[0]*(n+2)
    for _ in range(m):
        l,r=int(next(da)),int(next(da))
        inl=bisect.bisect_left(s,l)
        inr=bisect.bisect_right(s,r)
        diff[inl]+=1
        diff[inr]-=1
##        print(inl,inr)
    d,nan,x,b=0,0,0,0
    ls=0
    for i in range(1,n+1):
        ls+=diff[i]
        deff[i]+=ls
        if deff[i]%4==0:d+=1
        elif deff[i]%4==1:nan+=1
        elif deff[i]%4==2:x+=1
        elif deff[i]%4==3:b+=1

    
    print(d,nan,x,b)
if __name__=='__main__':
    solve()
