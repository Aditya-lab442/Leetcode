class Solution:
    def transpose(self, A: list[list[int]]) -> list[list[int]]:
        ans = []

        for i in A[0]:
            ans.append([i])
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                ans[j].append(A[i][j])
        return ans
