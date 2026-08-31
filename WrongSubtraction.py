x = list(map(int,input().split()))
n = x[0]
k = x[1]

for i in range(0,k):
    if n%10 == 0:
        f = int(str(n)[:-1])
        n = f
    else:
        n -= 1
print(n)

    