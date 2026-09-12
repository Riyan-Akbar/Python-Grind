tc = int(input())
for i in range (tc):
    rounds = int(input())
    game = list(map(int,input().split()))
    count1 = game.count(1)
    count0 = game.count(0)
    
    if count1 >= count0:
        print("Bessie")
    else:
        print("Elsie")

