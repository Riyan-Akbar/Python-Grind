import math
n, k, l, c, d, p, nl, np = map(int,input().split())
vol = k*l
toast = int(vol/nl)
limes = c*d
salt = int(p/np)
ans = min(toast,limes,salt)
toast = ans/n
print(math.floor(toast))