def narcissistic( value ):
    lt = len(list(str(value)))
    tempval = value
    print(lt)
    total = 0
    for i in range(lt):
        num = value % 10
        print(num)
        value = value // 10
        print(value)
        total = total + num**lt
        print(total)

    if tempval == total:
        return print(True)
    else:
        return print(False)

narcissistic(371)