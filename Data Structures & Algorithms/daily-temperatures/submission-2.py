class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        
        for i in range(n-2,-1,-1):
            j=i+1
            while j < n and temperatures[i] >= temperatures[j]:
                if ret[j] != 0:
                    j+=ret[j]
                else:
                    j=n

            print(i,j)
            if j<n:
                print(j-i)
                ret[i]=j-i
        return ret
        # stack = []
        
        # for i in range(len(temperatures)-1,-1,-1):
        #     if not stack:
        #         stack.append([temperatures[i],i])
        #     else:
        #         print(i, stack)
        #         top = stack[-1]
        #         while len(stack)>0 and top[0] <= temperatures[i]:
        #             stack.pop()
        #             if stack:
        #                 top = stack[-1]
        #         if top[0] > temperatures[i]:
        #             ret[i] = top[1]-i if top else 0
        #         stack.append([temperatures[i],i])
        #         print(i, stack)

        # return ret