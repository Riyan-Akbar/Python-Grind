ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
m = n = 3
if not ops:
    print(m*n)
else:
    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)
    print(min_a * min_b)