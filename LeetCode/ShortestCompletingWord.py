import re
licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
ans = licensePlate.lower()
word = re.sub(r'[^a-zA-Z]', '', ans)
answer = ""
need = {}
for ch in word:
    need[ch] = need.get(ch, 0) + 1
    
for i in words:
    count = {}
    for ch in i.lower():
        count[ch] = count.get(ch, 0) + 1
    valid = True

    for ch in need:
        if count.get(ch, 0)< need[ch]:
            valid = False
            break

    if valid:
        if answer == "" or len(i) < len(answer):
            answer = i
print(answer)