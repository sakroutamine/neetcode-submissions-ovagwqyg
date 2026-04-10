class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l = 0
        dic={}
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r],0)+1
            while (r-l+1) -max(dic.values()) > k:
                dic[s[l]]-=1
                l+=1
                
            result = max(result, r-l+1)

        return result 

