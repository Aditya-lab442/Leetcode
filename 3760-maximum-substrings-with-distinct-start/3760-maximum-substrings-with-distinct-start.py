class Solution:
    def maxDistinct(self, s: str) -> int:
        d1 = dict()
        ans = 0
        for i in s:
            if i not in d1:
                ans += 1
                d1[i] = 1
        return ans
