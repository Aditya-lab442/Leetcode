class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        
        ans = math.log(n, 3)
        return abs(ans - round(ans)) < 1e-10