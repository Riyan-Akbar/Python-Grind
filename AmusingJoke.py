def check():
    s1 = input()
    s2 = input()
    s = input()
    s3 = s1+s2
    s = sorted(s)
    s3 = sorted(s3)
    if s == s3:
        return print('YES')
    else:
        return print('NO')

check()