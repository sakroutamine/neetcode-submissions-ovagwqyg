class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            ret = 0
            if i >= len(text1) or j >= len(text2):
                return 0
            elif (i,j) in memo:
                return memo[(i,j)]
            elif text1[i] == text2[j]:
                res = dfs(i+1, j+1) + 1
            else:
                res = max(dfs(i+1, j), dfs(i, j+1))
            
            memo[(i,j)] = res
            return res
            

        lenmax = dfs(0,0)
        return lenmax