n = int(input())
# this code exceeded the time limit of codeforce
# res = 0
# for i in range(1,n+1):
#     func = ((-1)**i)*i  
#     res = res + func
# print(res)

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)