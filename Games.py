def clash(tc):
    count = 0
    home = []
    away = []
    for i in range(tc):
        h, a = map(int,input().split())
        home.append(h)
        away.append(a)
    for i in range (tc):
        for j in range(tc):
            if home[i] == away[j]:
                count += 1
    print(count)
    
n = int(input())
clash(n)

