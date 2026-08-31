numRooms = int(input())
countRooms = 0
for i in range(numRooms):
    x = list(map(int,input().split()))
    people = x[0]
    roomCap = x[1]

    if roomCap - people >= 2:
        countRooms +=1

print(countRooms)
