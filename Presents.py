totalFriends = int(input())
reciever = list(map(int,input().split()))
giver = []
for i in range(totalFriends):
    tg = i + 1
    idx = reciever.index(tg)
    giver.append(idx+1)
# the * operator when used with a list , it help to print a list with n spaced characters
print(*giver)