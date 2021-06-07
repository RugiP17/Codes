import sys
e=4
f=15
def eggdrop(e,f):
    if(f==0 or f==1):
        return f
    if(e==1):
        return f
    mn = sys.maxsize
    for k in range(1,f+1):
        temp=max(eggdrop(e,f-k),eggdrop(e-1,k-1))
        mn=min(temp,mn)
    return mn+1

print(eggdrop(e,f))