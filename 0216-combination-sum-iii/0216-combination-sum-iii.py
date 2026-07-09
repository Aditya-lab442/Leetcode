class Solution:
    ans = []

    def combinations(self, i, k, temp, nums, total, n, ans):
        if len(temp) == k:
            if sum(temp) == n:
                ans.append(temp[:])
            return
        if i == len(nums):
            return
        temp.append(nums[i])
        total += nums[i]
        self.combinations(i + 1, k, temp, nums, total, n, ans)
        total -= nums[i]
        temp.pop()
        self.combinations(i + 1, k, temp, nums, total, n, ans)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        ans = []
        self.combinations(0, k, [], nums, 0, n, ans)
        return ans
