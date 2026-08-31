x = int(input())
string = input().lower()

alpha = "abcdefghijklmnopqrstuvwxyz"
alphaSet = set(alpha)

res = set(string)
sorted(res)

if res == alphaSet:
    print("YES")
else:
    print("NO")


