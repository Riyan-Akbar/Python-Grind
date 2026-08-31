testCase = int(input())
ans = []
for i in range(testCase):
    n, m = map(int,input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    bea = int(a[0]) + n - 1
    ver = int(b[0]) + m - 1

    if bea >= ver:
        ans.append(1)
    else:
        ans.append(2)

for i in range(testCase):
    print(ans[i],end='\n')