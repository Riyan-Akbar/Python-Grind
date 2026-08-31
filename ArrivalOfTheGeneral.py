x = int(input())
heights = list(map(int,input().split()))

tallestIndex = heights.index(max(heights))
smallestIndex = len(heights) - 1 - heights[::-1].index(min(heights))

swapsMax = tallestIndex
swapsMin = (x - 1) - smallestIndex
totalSwaps = swapsMax + swapsMin

if tallestIndex > smallestIndex:
    totalSwaps = totalSwaps - 1

print(totalSwaps)
