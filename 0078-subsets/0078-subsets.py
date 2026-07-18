class Solution:
    def allSubsets(self, arr, ans, i, temp):
        if i == len(arr):
            ans.append(temp[:])
            return
        temp.append(arr[i])
        self.allSubsets(arr, ans, i + 1, temp)

        temp.pop()
        self.allSubsets(arr, ans, i + 1, temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.allSubsets(nums, ans, 0, [])
        return ans
