tc = int(input())
s = set("codeforces")
for i in range (tc):
    letter = input()
    if letter in s:
        print("yes")
    else:
        print("no")
