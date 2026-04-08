class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return max(1,n)

        num1, num2 = 1,2

        for i in range(2,n):
            cur = num1 + num2
            num1 = num2
            num2 = cur
        
        return num2
