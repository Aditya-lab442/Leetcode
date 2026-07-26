class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Prefix sums: pref[i] = sum of first i elements (indices 0..i-1)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        
        # Total absolute sum – upper bound for any possible left sum
        total_abs = sum(abs(x) for x in nums)
        
        # Suffix products with capping
        suff = [None] * (n + 1)
        suff[n] = 1  # product of empty set
        
        for i in range(n - 1, -1, -1):
            if suff[i + 1] is None:
                suff[i] = None
            else:
                prod = suff[i + 1] * nums[i]
                if abs(prod) > total_abs:
                    suff[i] = None   # product too large to match any left sum
                else:
                    suff[i] = prod
        
        # Check each index
        for i in range(n):
            left = pref[i]
            right = suff[i + 1]
            if right is not None and left == right:
                return i
        
        return -1
