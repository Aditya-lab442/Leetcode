class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        total = len(grid) * len(grid[0])
        temp1 = []
        temp2 = []
        k = k % total
        for i in grid:
            for j in i:
                if len(temp1) == total - k:
                    temp2.append(j)
                else:
                    temp1.append(j)
        temp1 = temp2 + temp1
        ptr = 0
        for i in range(len(grid)):
            temp3 = []
            for j in range(len(grid[i])):
                temp3.append(temp1[ptr])
                ptr += 1
            ans.append(temp3[:])
        return ans
