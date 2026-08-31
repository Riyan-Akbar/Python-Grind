people = int(input())
response = input().split()
flag = 0
for i in range(people):
    if response[i] == '1':
        flag = 1
        break
    
if flag == 1:
    print('HARD')
else:
    print('EASY')
