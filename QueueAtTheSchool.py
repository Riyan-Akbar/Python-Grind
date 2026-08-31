x = list(map(int,input().split()))
numChild = x[0]
time = x[1]
s = list(input())
# i should have used WHILE LOOP NOT FOR LOOP FOR THE INNER LOOP
# for j in range(time):
#     for i in range(numChild-1):
#         if s[i] == 'B' and s[i+1] == 'G':
#             temp = s[i]
#             s[i] = s[i+1]
#             s[i+1] = temp
#             i += 2
#         else:
#             i += 1
#         print(s)

for j in range(time):
    i=0
    while i < numChild-1:
        if s[i] == 'B' and s[i+1] == 'G':
            temp = s[i]
            s[i] = s[i+1]
            s[i+1] = temp
            i += 2
        else:
            i += 1

res = "".join(s)
print(res)


