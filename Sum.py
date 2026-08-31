total = int(input())
ans = []
for i in range(total):
    a, b, c = map(int,input().split())

    if a + b == c:
        ans.append('YES')
    elif a + c == b:
        ans.append('YES')
    elif b + c == a:
        ans.append('YES')
    else:
        ans.append('NO')

for i in range(len(ans)):
    print(ans[i],end='\n')
