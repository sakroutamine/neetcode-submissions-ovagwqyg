class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        l,r = 0,0
        maxlen = 0

        while r < len(s):
            print(l,r)
            while dic[s[r]]!=0:
                dic[s[l]]-=1
                l+=1
            dic[s[r]]+=1
            r+=1
                
            maxlen = max(maxlen,r-l)

        return maxlen
        
