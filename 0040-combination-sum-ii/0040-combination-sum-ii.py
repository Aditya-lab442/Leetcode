class Solution:
    def backtrack(self, start, target, temp, candidates, ans):
        if target == 0:
            ans.append(temp[:])
            return

        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # Pruning
            if candidates[i] > target:
                break

            temp.append(candidates[i])
            self.backtrack(i + 1, target - candidates[i], temp, candidates, ans)
            temp.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(0, target, [], candidates, ans)
        return ans