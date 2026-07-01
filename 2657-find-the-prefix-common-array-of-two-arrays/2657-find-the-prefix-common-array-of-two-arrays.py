class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            res = set(A[0 : i + 1]).intersection(B[0 : i + 1])
            ans.append(len(res))
        return ans
