class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        seccond = 0
        for i in nums:
            if i > first:
                second = first
                first = i
            elif second < i:
                second = i
        return (first - 1) * (second - 1)
