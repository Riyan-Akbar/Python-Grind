word = input()
count = 0

for char in word:
    if char.isupper():
        count += 1

if count > len(word)/2:
    res = word.upper()
    print(res)
else:
    res = word.lower()
    print(res)
