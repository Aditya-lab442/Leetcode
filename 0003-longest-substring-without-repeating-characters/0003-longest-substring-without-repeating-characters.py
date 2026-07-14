class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ansStr = ""
        for i in s:
            if i not in ansStr:
                ansStr += i
            else:
                ans = max(ans, len(ansStr))
                ansStr = ansStr[1::]
                while i in ansStr:
                    ansStr = ansStr[1::]
                ansStr += i
        return max(ans, len(ansStr))
