from math import factorial
numRows = 5
mat = []
for i in range (numRows):
    r = []
    for j in range(i+1):
        ncr = factorial(i)// (factorial(j) * factorial(i - j ))
        r.append(ncr)
    mat.append(r)
print(mat)
