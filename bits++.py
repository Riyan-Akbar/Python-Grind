n = int(input())
x = 0
for i in range (n):
    u = input()
    if u in ('++X', 'X++'):
        x += 1
    elif u in ('--X', 'X--'):
        x -= 1
print (x)

# import re
    # if re.fullmatch(r"^[+x]{3}$",u):
    # if u == '++x' or 'x++':

    # if re.fullmatch(r"^[-x]{3}$",u):
    # elif u == '--x' or 'x--':

    # if set(u).issubset({'x++', '++x'}):
    #     x += 1
    # elif set(u).issubset({'x++', '++x'}):
    #     x -= 1

# ^ and $ ensure the pattern matches the whole string exactly