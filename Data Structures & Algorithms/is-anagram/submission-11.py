class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = defaultdict(int)
        dic2=defaultdict(int)
        for i in range(len(s)):
            dic1[s[i]]+=1
            dic2[t[i]]+=1
        return dic1==dic2
