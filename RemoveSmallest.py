tc = int(input())
for i in range(tc):
    r = int(input())
    l = list(map(int,input().split()))
    
    l.sort()

    for i in range(r - 1):
        if abs(l[i] - l[i + 1]) > 1:
            print("NO")
            break
    else:
        print("YES")
    
    # i complicated it too much
    # l.sort()
    # l = list(set(l))

    # if len(l) == 1:
    #     print("YES")
    # else:
    #     for i in range(len(l) - 1):
    #         if abs(l[i] - l[i+1]) > 1:
    #             print("NO")
    #             break
    #     else:
    #         print("YES")