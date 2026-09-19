tc = int(input())
for i in range(tc):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        print('YES')
    elif k == 1 and len(set(nums)) != 1:
        if nums == sorted(nums):
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
            
        