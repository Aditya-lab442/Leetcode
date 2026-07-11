class Solution:
    def getAllCombination(self, arr, idx, tar, ans, combin):
        if tar == 0:
            ans.append(combin[:])
            return

        if idx == len(arr) or tar < 0:
            return

        combin.append(arr[idx])

        # include
        self.getAllCombination(arr, idx, tar - arr[idx], ans, combin)

        combin.pop()

        # exclude
        self.getAllCombination(arr, idx + 1, tar, ans, combin)

    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        ans = []
        self.getAllCombination(arr, 0, target, ans, [])
        return ans