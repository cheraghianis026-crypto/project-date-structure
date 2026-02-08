def tavan(n,m):
    if(m==1):
        return n
    else:
        return n*tavan(n,m-1)
n = int(input())
m = int(input())
print (tavan(n,m))