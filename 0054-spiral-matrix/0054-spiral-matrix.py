class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        srow = 0
        erow = m - 1
        scol = 0
        ecol = n - 1
        ans = []
        while srow <= erow and scol <= ecol:

            # top
            for i in range(scol, ecol + 1):
                ans.append(mat[srow][i])

            # right
            for i in range(srow + 1, erow + 1):
                ans.append(mat[i][ecol])

            # bottom
            for i in range(ecol - 1, scol - 1, -1):
                if srow == erow:
                    break
                ans.append(mat[erow][i])

            # left
            for i in range(erow - 1, srow, -1):
                if scol == ecol:
                    break
                ans.append(mat[i][scol])

            srow += 1
            erow -= 1
            ecol -= 1
            scol += 1
        return ans
