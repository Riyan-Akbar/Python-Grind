x = list(map(int, input().split()))
k = x[0] # cost of the first banana
n = x[1] # money he has with himself
w = x[2] # no. of banana he needs
res = 0
for i in range (1,w+1):
    money = k*i
    res = res + money

if res > n:
    finalRes = abs(n - res)
else:
    finalRes = 0 # i have to print if he has to borrow money or not if he does not have to borrow money print 0 else abs of n - res
print (finalRes)