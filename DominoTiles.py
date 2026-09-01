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