grid = ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
rows = len(grid)
cols = len(grid[0])
perimeter = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            continue
        perimeter += 4
        if i > 0 and grid[i - 1][j] == 1:
            perimeter -= 2
        if j > 0 and grid[i][j - 1] == 1:
            perimeter -= 2
print(perimeter)







# for i in range(rows):
#     for j in range(cols):
#         if grid[i][j] == 1:
#             top = grid[i - 1][j] if i > 0 else 0
#             bottom = grid[i + 1][j] if i < rows - 1 else 0
#             left = grid[i][j - 1] if j > 0 else 0
#             right = grid[i][j + 1] if j < cols - 1 else 0
#             perimeter += 4 - (top + bottom + left + right)
