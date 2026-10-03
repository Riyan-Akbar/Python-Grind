s = input()

ns = ""
i = 0

while i < len(s):

    if s[i] == ".":
        ns += "0"

    elif s[i:i+2] == "-.":
        ns += "1"
        i += 1

    elif s[i:i+2] == "--":
        ns += "2"
        i += 1

    i += 1

print(ns)