class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs)==0:
            return ""
        strs.sort()

        ret = ""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]==strs[-1][i]:
                ret += strs[0][i]
            else:
                return ret

        return ret