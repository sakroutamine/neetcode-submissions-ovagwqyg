class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums, curr = max(nums),0
        l = 0

        for r in range(len(nums)):
            print(l,r,sums,curr)
            if nums[r] > curr+nums[r]:
                sums = max(nums[r], sums)
                curr = nums[r]
                l=r
            else:
                curr+= nums[r]
            sums =max(sums,curr)
        
        return max(curr,sums)
        

 