class Solution:
    def all(self, i, temp, nums, ans, k):
        if len(temp) == k:
            ans.append(temp[:])
            return
        if i == len(nums):
            return
        temp.append(nums[i])
        self.all(i + 1, temp, nums, ans, k)
        temp.pop()
        self.all(i + 1, temp, nums, ans, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = list(range(1, n + 1))
        self.all(0, [], temp, ans, k)
        return ans
