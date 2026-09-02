tc = int(input())
ans = []
for i in range(tc):
    length = int(input())
    a = input()
    b = input()
    tempa = list(a)
    tempb = list(b)

    countodda = 0
    countevena = 0
    countoddb = 0
    countevenb = 0

    for i in range(0,length,2):
        if tempa[i] == '1':
            countevena += 1
    for i in range(1,length,2):
        if tempa[i] == '1':
            countodda += 1

    for i in range(0,length,2):
        if tempb[i] == '1':
            countevenb += 1
    for i in range(1,length,2):
        if tempb[i] == '1':
            countoddb += 1
            
    if countodda == countoddb and countevena == countevenb:
        ans.append('yes')
    else:
        ans.append('no')


for i in range(len(ans)):
    print(ans[i],end="\n")


# Rating: 1000

# What was the main idea? : the main idea was to count the number of 1's at odd and even places in both the string

# What did I initially think? i initially thought of replacing the characters and then matching it, which was a good initial idea but bad for large scale

# Where did I get stuck? i got stuck in the logic, as i was doing a complex replacing algo where as it was just counting the no of 1's 

# What observation unlocked it? : figured it out with the help of ai, was doing it in some different way

# What technique was used? one loop in which the inputs where taken and  the no of 1's were counted

# Could I recognize this technique in another problem? : no this was the first time i faced this type of problem.   

            


