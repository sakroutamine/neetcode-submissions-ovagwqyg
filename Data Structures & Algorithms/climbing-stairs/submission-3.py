class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return max(n,1)
            
        l1,l2 = 1,1

        for i in range(n):
            l2,l1 = l1, l1+l2
        return l2