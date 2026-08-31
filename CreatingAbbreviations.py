testCases = int(input())

for i in range(testCases):
    finalRes = []
    
    word = []
    abb = []
    n, m = map(int,input().split())

    for i in range(n):
        ins = input()
        res = ins[0:1]
        word.append(res)
        newWord = list(sorted(set(word)))
    # print(newWord)

    for j in range(m):
        abb.append(input().lower())
        result = [char for item in abb for char in item]
        # print(result)
        newRes = list(set(result))
    # print(newRes)

    for char in newRes:
        if char in newWord:
            finalRes.append(1)
        else:
            finalRes.append(2)
    # print(finalRes)
    
    final = list(set(finalRes))
    # print(final)

    if 2 in final:
        print("NO")
    else:
        print("YES")


