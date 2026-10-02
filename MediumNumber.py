tc = int(input())
for i in range(tc):
    l = list(map(int, input().split()))
    l.sort()
    t = len(l)
    if t % 2 == 0:
        lm = len(l) // 2
        rm = lm + 1
        print((l[lm] + l[rm])//2)
    else:
        lm = len(l) // 2
        print(l[lm])