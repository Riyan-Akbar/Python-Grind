x = int(input())

lt = input()

count = 0

for i in range(1,x):
    if lt[i] == lt[i-1]:
        count += 1
print (count)

# i = 0
# while i < x:
#     if lt[i] == lt[i-1]:
#         lt.pop(i)
#         count += 1
# print (len(lt))


"this is the sol i copied from ai . FUCK AI , i aint stupid this coding language is stuipd."
# n = int(input())
# stones = input()

# count = 0

# for i in range(1, n):
#     if stones[i] == stones[i - 1]:
#         count += 1

# print(count)