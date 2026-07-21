class Solution:
    def largestRectangleArea(self, ht: List[int]) -> int:
        n = len(ht)
        right = [0] * n
        left = [0] * n
        stack = []
        # right smaller

        for i in range(len(ht) - 1, -1, -1):
            while len(stack) > 0 and ht[stack[-1]] >= ht[i]:
                stack.pop()
            right[i] = n if len(stack) == 0 else stack[-1]
            stack.append(i)

        stack.clear()
        # left smaller

        for i in range(len(ht)):
            while len(stack) > 0 and ht[stack[-1]] >= ht[i]:
                stack.pop()
            left[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(i)

        # answer

        ans = 0

        for i in range(len(ht)):
            area = ht[i] * (right[i] - left[i] - 1)
            ans = max(ans, area)
        return ans
