horseshoe = list(map(int,input().split()))
distinctShoe = set(horseshoe)
res = len(horseshoe) - len(distinctShoe)
print(res)