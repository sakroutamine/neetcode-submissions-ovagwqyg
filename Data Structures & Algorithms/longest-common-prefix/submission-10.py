class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        st = ""
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            st += strs[0][i]
        return st













































        # strin = sorted(strs)
        # for i in range(len(strin[0])):
        #     print("iloc", i)
        #     if strin[0][i] != strin[-1][i]:
        #         return strin[0][0:i]
        # return strin[0]