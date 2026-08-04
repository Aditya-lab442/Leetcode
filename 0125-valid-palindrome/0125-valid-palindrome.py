class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
        print(ans)
        return "".join(ans) == "".join(ans[-1::-1])
