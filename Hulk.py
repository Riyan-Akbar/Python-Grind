n = int(input())
hate ="I hate"
love = "I love"
lst = []

for j in range(1,n+1):
    if j%2 == 0:
        lst.append(love)
    else:
        lst.append(hate)
    if j != n:
        lst.append(" that ")

lst.append(" it")
res = "".join(lst)
print(res)

