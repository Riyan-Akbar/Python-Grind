digits = [4,3,2,1]
result = int(''.join(map(str, digits)))
result += 1
ans = [int(digit) for digit in str(result)]
print(ans)
