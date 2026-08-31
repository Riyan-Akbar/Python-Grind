orangeContaining = int(input())
vols = list(map(int,input().split()))
totalVols = sum(vols)
res = totalVols / orangeContaining
print(f"{res:.14f}")