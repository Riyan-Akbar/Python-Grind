tc = int(input())
for i in range(tc):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = a.count(k)
    if count >= 1:
        print("YES")
    else:
        print("NO")