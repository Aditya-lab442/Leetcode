class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = dict()
        ans = []
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in d1:
                d1[temp] = [i]
            else:
                d1[temp].append(i)
        for i, j in d1.items():
            temp = []
            for k in j:
                temp.append(strs[k])
            ans.append(temp)
        return ans
