t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k < n or k > 2 * n - 1:
        print(-1)
        continue


    a = [[0] * n for _ in range(n)]


    components = 2*n - k
    num = 1

    for i in range(components - 1):
            a[i][i] = i + 1
            num += 1

    start = components - 1

    for i in range(start, n):
        a[i][i] = num
        num += 1

        if i + 1 < n:
            a[i + 1][i] = num
            num += 1


    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                a[i][j] = num
                num += 1

    for row in a:
        print(*row)

    