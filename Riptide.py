# def riptide():
#     # count = 0

#     tc = int(input())
#     for i in range(tc):
#         x = list(map(int,input().split()))
#         x = sorted(x)


#         if x[0] == x[1] or x[1] == x[2] or x[0] == x[2]:
#             print(0)
#         elif (x[1] + 2) == x[2]:
#             print(1)
#         else:
#             print(abs(x[1]-x[2]))
#             bol = True
#             while(bol):
#                 x[0] = x[0] + 1
#                 x[2] = x[2] - 1
#                 if (min(x[1] - x[0],x[2] - x[1])):
#                     bol = False
#                     print((min(x[1] - x[0],x[2] - x[1])))
#             #     print
#             #     if x[1] == x[2]:
#             #         bol = False
#             # print(count)
            
    # bol = True
    # while(bol):
    #     x[0] = x[0] + 1
    #     x[2] = x[2] - 1
    #     if (min(x[1] - x[0],x[2] - x[1])):
    #         bol = False
    #     print(abs((min(x[1] - x[0],x[2] - x[1]))))
        
def riptide():
    # count = 0
    tc = int(input())
    for i in range(tc):
        x = list(map(int,input().split()))
        x = sorted(x)
        print(abs((min(x[1] - x[0],x[2] - x[1]))))
riptide()