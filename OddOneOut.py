from collections import Counter
tc = int(input())
for _ in range(tc):
    l = list(map(int, input().split()))
    counter = Counter(l)
    for num, count in counter.items():
        if count == 1:
            print(num)
            break
