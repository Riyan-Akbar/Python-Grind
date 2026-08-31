string = list(input())
lst = []
for char in string:
    if char.lower() == "g":
        lst.append('G')
    elif char.lower() == ")":
        lst.append('o')
    elif char == 'a':
        lst.append('al')
lst.pop()
print("".join(lst))