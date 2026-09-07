def move_zeros(lst):
    pos = 0
    for i in range(len(lst)):
        if lst[i] !=0:
            lst[pos],lst[i] = lst[i],lst[pos]
            pos += 1
    return print(lst)
move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])