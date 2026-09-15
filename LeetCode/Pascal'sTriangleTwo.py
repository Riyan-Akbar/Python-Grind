from math import factorial
rowIndex = 3
mat = []
for i in range (rowIndex+1):
    ncr = factorial(rowIndex)// (factorial(i) * factorial(rowIndex - i))
    mat.append(ncr)
print(mat)
