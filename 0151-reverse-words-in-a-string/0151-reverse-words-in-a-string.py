class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        ans = ""
        temp = ""
        ansList = list()
        s = s.strip()
        for i in s:
            if i.isalnum():
                temp += i
            else:
                if temp == "":
                    continue
                ansList.append(temp)
                temp = ""
        ansList.append(temp)

        for i in ansList[-1::-1]:
            ans += i + " "
        return ans.strip()
