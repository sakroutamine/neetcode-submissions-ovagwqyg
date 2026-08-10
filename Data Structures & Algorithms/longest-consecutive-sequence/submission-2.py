class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        maxs = 0

        for i in nums:
            if (i-1) not in sets:
                lent = 0
                while (i+lent) in sets:
                    lent+=1
                maxs=max(lent,maxs)

        
        return maxs