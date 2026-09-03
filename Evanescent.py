tt = int(input())
ans = []
"""
Note this is logically correct but its a brute force way, now i need to find a way were i dont need to store these values instead i will count them

for i in range(tt):
    l = int(input())
    s = list(input())
    curptr = 1
    for i in range(1,l-1):
        ns = s.copy()
        ns.pop(i)
        ptr = 1
        for j in range(1,len(ns)):
            if ns[j] != ns[j - 1]:
                ptr +=1
        if ptr < curptr:
            curptr = ptr
    ans.append(curptr)

for i in range(len(ans)):
    print(ans[i],end="\n")

"""


for _ in range(tt):

    n = int(input())
    s = input()

    # Original compressed length
    cur = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            cur += 1

    best = cur

    # Try deleting every allowed character
    for i in range(1, n - 1):

        new_len = cur

        # Remove the two old connections
        if s[i] != s[i - 1]:
            new_len -= 1

        if s[i] != s[i + 1]:
            new_len -= 1

        # Add the new connection
        if s[i - 1] != s[i + 1]:
            new_len += 1

        best = min(best, new_len)

    ans.append(best)

for x in ans:
    print(x)
        