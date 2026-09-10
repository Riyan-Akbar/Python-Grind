l = ["alice,50,sf","alice,60,ny","ali,50,ind","alice,50,ind"]
p = []
for i in range(len(l)):
    temp = l[i].split()
    p.append(temp)
print(p)