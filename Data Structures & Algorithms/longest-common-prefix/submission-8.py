class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strin = sorted(strs)
        for i in range(len(strin[0])):
            print("iloc", i)
            if strin[0][i] != strin[-1][i]:
                return strin[0][0:i]
        return strin[0]