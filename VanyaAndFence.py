x = list(map(int,input().split()))
numFri = x[0]
heights = x[1]

y = list(map(int,input().split()))

count = 0

for i in range(numFri):
    if y[i] > heights:
        count += 2
    else:
        count += 1

print (count)
