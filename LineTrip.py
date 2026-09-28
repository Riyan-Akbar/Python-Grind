tc = int(input())
for i in range(tc):
    n, end = map(int,input().split())
    arr = list(map(int, input().split()))
    temp = []
    temp.append(arr[0])

    for i in range(0,n - 1):
        ans = abs(arr[i] - arr[i+1])
        temp.append(ans)
    t1 = max(temp)
    t2 = 2 * (end - arr[-1])
    ans = max(t1,t2)
    print(ans)

