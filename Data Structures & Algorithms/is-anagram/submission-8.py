class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici = {}
        dicj={}
        for i in s:
            dici[i] = 1+ dici.get(i,0)
        for j in t:
            dicj[j] = 1+ dicj.get(j,0)
        return dici==dicj

































    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     ss, tt= {}, {}

    #     for i in range(len(s)):
    #         ss[s[i]]= ss.get(s[i], 0) + 1
    #         tt[t[i]]= tt.get(t[i], 0) + 1
    #     print(ss, tt)
    #     return ss==tt