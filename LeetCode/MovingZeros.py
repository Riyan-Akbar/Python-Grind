nums = [0,0,1]
# c = 0
# l = len(nums)
# for i in range(l):
#     if nums[i] != 0:
#         nums[c] = nums[i]
#         c += 1

# for i in range(c,l):
#     nums[i] = 0

# print(nums)

for i in range(len(nums)):
    if nums[i] == 0:
        nums.remove(nums[i])
        nums.append(0)
print(nums)
