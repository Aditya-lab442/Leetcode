class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq = [0] * 26
        for i in s1:
            freq[ord(i) - ord("a")] += 1
        print(freq)
        windowFr = [0] * 26
        j = 0
        k = len(s1) - 1
        while k < len(s2):
            temp = s2[j : k + 1]
            for i in temp:
                windowFr[ord(i) - ord("a")] += 1
            if windowFr == freq:
                return True
            j += 1
            k += 1
            windowFr = [0] * 26
        return False
