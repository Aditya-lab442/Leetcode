class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = 0
        while n != 0:
            if n % 10 != 0:
                temp = temp * 10 + n % 10
            n //= 10
        n = temp
        temp = 0
        ans = 0
        while n != 0:
            temp = temp * 10 + n % 10
            ans += n % 10
            n //= 10

        return ans * temp
