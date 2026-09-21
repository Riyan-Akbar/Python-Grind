t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(1, n):
        if s[i - 1] == '1' and s[i] == '0':
            ans += 1

    print(ans)