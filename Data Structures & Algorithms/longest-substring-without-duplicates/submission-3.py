class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        inStr = set()
        l=0

        for r in range(len(s)):
            while s[r] in inStr:
                inStr.remove(s[l])
                l+=1
            inStr.add(s[r])
            longest = max(longest, r-l+1)
        return longest
