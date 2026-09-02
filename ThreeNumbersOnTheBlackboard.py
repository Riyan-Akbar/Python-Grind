tc = int(input())

res = []
for i in range(tc):
    s = list(map(int,input().split()))
    s = sorted(s)
    a = s[0]
    b = s[1]
    c = s[2]
    ans = min(c - a,b)
    res.append(ans)

for i in range (len(res)):
    print(res[i],end= "\n")