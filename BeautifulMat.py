matrix = []
for i in range(5):
    row = list(map(int, input().split()))
matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r = i
            c = j
            
answer = abs(r-2) + abs(c - 2)
print(answer)
            
