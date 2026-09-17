tc = int(input())
for i in range(tc):
    rt = int(input())
    if rt >= 1900:
        print("Division 1")
    elif 1600 <= rt <= 1899:
        print("Division 2")
    elif 1400 <= rt <= 1599:
        print("Division 3")
    else:
        print("Division 4")

        