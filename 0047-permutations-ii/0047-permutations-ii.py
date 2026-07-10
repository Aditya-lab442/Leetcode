class Solution:
    def backtrack(self, idx, nums, ans):
        if idx == len(nums):
            ans.append(nums[:])
            return

        used = set()

        for i in range(idx, len(nums)):
            if nums[i] in used:
                continue

            used.add(nums[i])

            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(idx + 1, nums, ans)
            nums[idx], nums[i] = nums[i], nums[idx]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(0, nums, ans)
        return ans