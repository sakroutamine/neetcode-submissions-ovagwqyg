class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sums = 0
        tmp = 0

        for i in nums:
            
            if i == 1:
                tmp+=1
            else:
                if tmp > sums:
                    sums = tmp
                tmp = 0
        if tmp > sums:
            sums = tmp
        return sums