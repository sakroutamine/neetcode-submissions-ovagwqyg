class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(ss)):
            if ss[i] != tt[i]:
                return False
        return True

                
        