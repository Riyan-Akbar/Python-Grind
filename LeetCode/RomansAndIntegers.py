class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        last = 0
        s = list(s)
        for ch in reversed(s):
            val = myd[ch]
            if val < last:
                ans -= val
            else:
                ans += val
            last = val
        return ans
            
myd = {"I": 1, "V": 5, "X": 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000}
