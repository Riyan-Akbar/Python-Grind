n = int(input())
digiLen = []

for i in range(n):
    digiLen.append(int(input()))

for i in range(n):
    num = digiLen[i]

    roundNums = []
    place = 1

    for j in range(len(str(num))):

        lastDigit = num % 10

        if lastDigit != 0:
            roundNums.append(lastDigit * place)
        num = num // 10
        place = place * 10
    print(len(roundNums))
    print(*roundNums)

        

