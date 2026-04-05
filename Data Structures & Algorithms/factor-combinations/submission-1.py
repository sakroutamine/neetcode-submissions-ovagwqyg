class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def factor(num, ans):
            if ans:
                ret.append(ans + [num])

            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0:
                    if not ans or i >= ans[-1]:
                        factor(num // i, ans+[i])

        ret = []   
        factor(n,[])              
        return ret