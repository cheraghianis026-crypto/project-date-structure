def tavan(n,m):
    if(m==1):
        return n
    elif (m==0):
        return 1
    else:
        return n*tavan(n,m-1)
n = int(input())
m = int(input())

print (tavan(n,m))
