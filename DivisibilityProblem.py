
noNums = int(input())

for i in range(noNums):
    a, b = map(int, input().split())

    remainder = a % b

    if remainder == 0:
        print(0)
    else:
        print(b - remainder)

        
# noNums = int(input())
# res = []
# for i in range(noNums):
#     count = 0
#     x = list(map(int,input().split()))
#     a = x[0]
#     b = x[1]
    
#     if a%b != 0:
#         count = b - (a%b)
#     res.append(count)

# for i in range(noNums):
#     print(res[i],end="\n")