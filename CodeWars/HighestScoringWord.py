def high(x):
    s = x.split()
    print(s)
    temp = []
    for i in range (len(s)):
        print(s[i])
        count = 0
        for ch in s[i]:
            print(ch)
            count = count + ord(ch) - 96
            print(count)
        temp.append(count)
        print(temp)
    h = temp.index(max(temp))
    print(h)
    return print(s[h])

high('man i need a taxi up to ubud')