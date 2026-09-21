tc = int(input())
for _ in range(tc):
    a, b, c = map(int, input().split())

    if a >= b:
        ans = a -b + c
    else:
        d = b - a
        ans = max(d,abs(c - d))
    print(ans)
