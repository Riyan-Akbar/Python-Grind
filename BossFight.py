# i am able to understand this problem but couldnt code it , and my apporach was way too complex.
tc = int(input())

for _ in range(tc):
    n = int(input())
    cards = list(map(int, input().split()))

    # Count frequencies
    counts = {}

    for x in cards:
        counts[x] = counts.get(x, 0) + 1

    # Find the most frequent damage
    max_value = max(counts, key=counts.get)
    max_count = counts[max_value]

    # If we can arrange everything without equal adjacent cards
    if max_count <= (n + 1) // 2:
        print(sum(cards))

    else:
        # Number of cards that are NOT max_value
        others = n - max_count

        # We can arrange:
        # max, other, max, other, ..., max
        # and then one more max triggers the shield.
        answer = sum(cards) - max_count * max_value
        answer += (others + 2) * max_value

        print(answer)









