from collections import Counter
tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    counter = Counter(l)
    for num, count in counter.items():
        if count == 1:
            print(l.index(num)+1)
            break
