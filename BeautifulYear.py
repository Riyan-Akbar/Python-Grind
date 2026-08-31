year = int(input())
year +=1 
while True:
    x = str(year)
    y = len(set(x))
    if y != 4:
        year += 1
    else:
        print(year)
        break


