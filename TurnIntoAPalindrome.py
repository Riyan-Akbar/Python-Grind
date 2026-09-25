tc = int(input())
for _ in range(tc):
    n, c = input().split()
    n = int(n)
    s = input()
    count = 0
    if s == s[::-1]:
        print(0)
    else:
        s = list(s)
        rs = s[::-1]
        for i in range(n // 2):
            if s[i] == s[n - 1 - i]:
                continue
            elif s[i] == c or s[n - 1 - i] == c:
                count += 1
            else:
                count += 23
        print(count)


