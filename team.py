n = int(input())
total = 0
for i in range (n):
    u = input().split()
    # if len(u) == 3 and set(u).issubset({'0', '1'}): -> this will not work as len of "1 0 1" will result in 5 digits rather than 3 and we dont need to specify subsets of digits as the input will always be 1 and 0 not any other no.
    ds = sum(map(int, u)) 
    if ds >= 2:
        total = total + 1
print(total)