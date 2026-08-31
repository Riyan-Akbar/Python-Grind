money = int(input())
count = 0

for note in [100,20,10,5,1]:
    count += money // note
    money = money%note

print(count)