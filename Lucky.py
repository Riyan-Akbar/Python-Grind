tc = int(input())

for i in range(tc):
    num = input()
    num = list(map(int, num))
    l = sum(num[0:3])
    r = sum(num[3:len(num)])
    if l == r:
        print("Yes")
    else:
        print("No")
