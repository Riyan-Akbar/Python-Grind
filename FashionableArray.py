tc = int(input())

for _ in range(tc):

    n = int(input())
    a = list(map(int, input().split()))

    freq = {}

    for x in a:
        freq[x] = freq.get(x, 0) + 1

    ans = []

    max_freq = max(freq.values())

    for k in range(1, max_freq + 1):

        for x in sorted(freq, reverse=True):

            if freq[x] >= k:
                ans.append(x)

    print(*ans)