# This is for codewars:
def square_digits(num):
    # Your code here
    tt = [int(i) for i in str(num)]
    for i in range(len(tt)):
        tt[i] = int(tt[i])*int(tt[i])
    return int("".join(map(str,tt)))
# This is for Myself:
def square_digits(num):
    # Your code here
    tt = [int(i) for i in str(num)]
    for i in range(len(tt)):
        tt[i] = int(tt[i])*int(tt[i])
    return print(int("".join(map(str,tt))))

square_digits(9119)

