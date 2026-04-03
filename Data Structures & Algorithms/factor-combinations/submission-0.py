import math

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ret = []


        def factor(num, start, curr):
            for i in range(start, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    ret.append(curr + [i, num // i])
                    factor(num // i, i, curr + [i])
            
        if n > 1:
            factor(n, 2, [])
        return ret