class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]

        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])

        return dp[0][0]
        # memo = {}

        # def sub(i,j):
        #     ret = 0
        #     if i >= len(text1) or j >= len(text2):
        #         ret = 0
        #     elif (i,j) in memo:
        #         ret = memo[(i,j)]
        #     elif text1[i] == text2[j]:
        #         ret = sub(i+1, j+1) + 1
        #         memo[(i,j)] = ret
        #     else:
        #         ret = max(sub(i+1,j), sub(i,j+1)) 

        #     memo[(i,j)] = ret
        #     return ret


        # return sub(0,0)





        # memo = {}
        # def dfs(i, j):
        #     ret = 0
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     elif (i,j) in memo:
        #         return memo[(i,j)]
        #     elif text1[i] == text2[j]:
        #         res = dfs(i+1, j+1) + 1
        #     else:
        #         res = max(dfs(i+1, j), dfs(i, j+1))
            
        #     memo[(i,j)] = res
        #     return res
            
        # lenmax = dfs(0,0)
        # return lenmax