nums = list(map(int, input().split()))
nums.sort()
a, b, c, k = nums[0], nums[1], nums[2], nums[3]

if a + b == a + c == b + c:
    a = b = c = abs(k - a)
    print(a, b, c)
else:
    temp = k
    x = abs(temp - c)
    y = abs(temp - b)
    z = abs(temp - a)
    print(x, y, z)