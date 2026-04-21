class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        nums.sort()
        for i,x in enumerate(nums):
            if i != x:
                return i
        return len(nums)