lb = list(map(int, input().split()))
count = 0
x = lb[0]
y = lb[1]
while True:
    if x <= y:
        x = x*3
        y = y*2
        count += 1
    else:
        break
print (count)