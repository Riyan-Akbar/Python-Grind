arr = [1,2,3,4,5,6,7,8,9,10]
k = 3

temp = []

for i in range(0,len(arr),k):
    temp = temp + arr[i:i+k][::-1]

print(temp)