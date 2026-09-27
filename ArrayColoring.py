tc = int(input())
for i in range(tc):
    r = int(input())
    l = list(map(int, input().split()))
    total = sum(l)
    if total % 2 == 0:
        print("YES")
    else:
        print("NO")