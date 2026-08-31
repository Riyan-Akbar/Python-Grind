# in codeforces you have to do everything from inputs to logic plus output

w = int(input(),2)
for i in range (w):
    st = input()
    x = len(st)
    if x <= 10:
        print(st)
    else:
        inbtw = len(st[1:-1])  
        print(st[0:1] + str(inbtw) + st[-1])