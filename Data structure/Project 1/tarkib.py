def tarkib(n,m):
    if m == 0 or m==n :
        return 1
    else :
        return tarkib(n-1,m)+tarkib(n-1,m-1)
n= int(input())
m= int(input())
print(tarkib(n,m))
