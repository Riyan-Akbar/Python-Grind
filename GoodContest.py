tc = int(input())
for _ in range(tc):
    n = int(input())
    sp = list(map(int, input().split()))

    ans = n - min(sp)
    print(ans)