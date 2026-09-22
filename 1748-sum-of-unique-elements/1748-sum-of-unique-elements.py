class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        temp = []
        for i in nums:
           if nums.count(i)==1:
            temp.append(i)
        return sum(temp)