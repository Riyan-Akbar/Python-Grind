n, m = map(int,input().split())
hrs = 240
rm = hrs - m
c = 0
t = 0
for i in range(1,n+1):
    pqt = 5*i
    t = t + pqt
    if t <= rm:
        c = c+1

print(c)

