class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = ""
        xStr = []
        yStr = []
        for i in s:
            if i == x:
                xStr.append(i)
            elif i == y:
                yStr.append(i)
            else:
                ans += i
        ans += "".join(yStr)
        ans += "".join(xStr)
        return ans
