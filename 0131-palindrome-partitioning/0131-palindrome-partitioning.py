class Solution:
    def getAllPart(self, st, partition, ans):
        if len(st) == 0:
            ans.append(partition[:])
            return
        for i in range(len(st)):
            part = st[: i + 1]
            if part[::] == part[::-1]:
                partition.append(part)
                self.getAllPart(st[i + 1 :], partition, ans)
                partition.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []
        self.getAllPart(s, partition, ans)
        return ans
