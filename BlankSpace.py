tc =int(input())
for i in range(tc):
    n = int(input())
    l = list(map(int,input().split()))
    current = 0
    ans = 0

    for x in l:
        if x == 0:
            current += 1
            ans = max(ans, current)
        else:
            current = 0
    print(ans)
