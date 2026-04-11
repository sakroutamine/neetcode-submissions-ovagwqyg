class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return max(n,1)
            
        l1,l2 = 2,1

        for i in range(2,n):
            temp = l1
            l1 = l1+l2
            l2 = temp
        return l1