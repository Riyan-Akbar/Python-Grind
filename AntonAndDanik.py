# count is the func called as to count something without looping as the function loops in c which is obiously faster

noGames = int(input())
gamesList = input()
countA = gamesList.count('A')
countD = gamesList.count('D')
if countA > countD:
    print('Anton')  
elif countA < countD:
    print('Danik')
else:
    print('Friendship')