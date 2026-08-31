m = input().split()
n = int(m[0])
k = int(m[1])
mr = input().split()
scores = [int(x) for x in mr]
ct = scores[k-1]
total = 0
for i in scores:
    if i > 0 and i >= ct:
        total += 1
print (total)


# Another apporach --------------------->
# total = 0
# for i in range(0,n):
#     # if the initial value of the list is zero then the whole total is zero
#     if scores[i] == 0:
#         break
#     else:
#         if scores[i] > 0 and i+1 <=k: // this  stupid i+1 <= k is important for checking the position of i+1 is less than or equal to k
#             total += 1
#         else:
#             if scores[i] == scores[k-1]:
#                 total += 1
#             else:
#                 break
# print(total)