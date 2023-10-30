class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = collections.Counter(s1)
        for i in range(len(s2)-len(s1) + 1):
            s = s2[i:i+len(s1)]
            count2 = collections.Counter(s)
            if count1==count2:
                return True
        return False