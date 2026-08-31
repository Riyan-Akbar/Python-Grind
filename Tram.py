stops = int(input())
stack = []
maxCap = 0
currentCap = 0
for i in range(stops):
    x = list(map(int,input().split()))
    entered = x[1]
    exited = x[0]
    currentCap = currentCap - exited + entered
    if currentCap > maxCap:
        maxCap = currentCap
print(maxCap)