testCase = int(input())

for _ in range(testCase):

    ans = 0

    length = int(input())
    s = input()

    # Four possible first two characters
    patterns = ["00", "01", "10", "11"]

    for pattern in patterns:

        candidate = list(pattern)

        # Generate the rest of the pattern
        for i in range(2, length):
            if candidate[i - 2] == '0':
                candidate.append('1')
            else:
                candidate.append('0')

        # Check candidate against original string
        valid = True

        for i in range(length):
            if s[i] != '?' and s[i] != candidate[i]:
                valid = False
                break

        if valid:
            ans += 1

    print(ans)


# Rating: 1000

# What was the main idea? : the main idea was to create a pattern where ith pos != [i-2]th pos and only 4 pattern needed to be created using 00,01,11,10.

# What did I initially think? i was unable to understand the idea first but with help i could understand the basics of what i need to do

# Where did I get stuck? i got stuck in programing the main logic where i need to generate the pattern of the input length of the string while also match it condintion of the input string.

# What observation unlocked it? : youtube video of some iit bhu dude helped me unlock the idea , i couldnt 

# What technique was used? only one loop where the patterns were generated and then checked with the input string.

# Could I recognize this technique in another problem? : no this was the first time i faced this type of problem.   