x = list(map(int, input().split()))
m = x[0]
n = x[1]

tile = m*n

if tile%2 == 0:
    print (int (tile/2))
else:
    print (int(tile/2))

