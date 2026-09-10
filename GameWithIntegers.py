tc = int(input())
for i in range(tc):
    num = int(input())
    count = 0
    for i in range(11):
        flag = False
        if i == 11:
            print("Second")
            break
        if (num + 1) % 3 == 0 or (num - 1) % 3 == 0:
            flag = True
    if flag:
        print("First")
    else:
        print("Second")
