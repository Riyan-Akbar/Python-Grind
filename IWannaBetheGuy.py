tt1 = int(input())
x = list(map(str,input().split()))
y = list(map(str,input().split()))
x.pop(0)
y.pop(0)

DuplicateTotal = x + y

ActualTotal = sorted(set(DuplicateTotal))
ActualTotal = list(map(int,ActualTotal))

if len(ActualTotal) == tt1:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
