def ranks(score):
    ts = score.copy()
    ts.sort(reverse=True)

    fl = [""] * len(score)

    for rank, i in enumerate(ts):
        pos = score.index(i)

        if rank == 0:
            fl[pos] = "Gold Medal"
        elif rank == 1:
            fl[pos] = "Silver Medal"
        elif rank == 2:
            fl[pos] = "Bronze Medal"
        else:
            fl[pos] = str(rank + 1)

    return fl


a = ranks([5, 4, 3, 2, 1])
b = ranks([10, 3, 8, 9, 4])

print(a)
print(b)