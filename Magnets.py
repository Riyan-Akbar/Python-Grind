numMag = int(input())
mags = []

for i in range(numMag):
    mags.append(input())

fiMag = mags[0]
grp = 1

for i in range(1,numMag):
    if mags[i] != mags[i-1]:
        grp += 1
    mags[i-1] = mags[i]

print(grp)
