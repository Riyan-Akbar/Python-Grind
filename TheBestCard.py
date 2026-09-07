tc = int(input())
for _ in range(tc):
    tt = int(input()) + 1
    prime = True
    for  i in range(2, int(tt**0.5)+1):
        if tt % i == 0:
            prime = False
            break
    if prime:
        print('yes')
    else:
        print('no')

# thought of the program correctly but find it hard to code the logic as i didnt knew the divisibility math properly(i mean the number theory).
