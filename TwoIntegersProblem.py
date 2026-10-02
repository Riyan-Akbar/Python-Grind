tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())

    diff = abs(a - b)

    ans = (diff + 9) // 10

    print(ans)