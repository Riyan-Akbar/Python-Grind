tc = int(input())
for _ in range(tc):
    score = list(map(int, input().split()))
    timur = score[0]
    score.sort(reverse=True)
    pos = score.index(timur)
    print(pos)