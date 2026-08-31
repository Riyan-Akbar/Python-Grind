n = int(input())
name = []
for i in range (n):
    name.append(input())

faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

count = 0

for i in range(n):
    count += faces[name[i]] # new type of thing in dictionary and list loop checking keys and list then adding values to count total

print(count)