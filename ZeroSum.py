tc = int(input())

for _ in range(tc):
    n = int(input())
    ls = list(map(int, input().split()))

    countNeg = 0

    for x in ls:
        if x == -1:
            countNeg += 1

    if n % 2 == 0 and countNeg % 2 == (n // 2) % 2:
        print("YES")
    else:
        print("NO")