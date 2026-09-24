tc = int(input())
for _ in range(tc):
    n = int(input())
    t = 0
    for i in range(1):
        t = n % 10
        n = n // 10
        t += n
    print(t)