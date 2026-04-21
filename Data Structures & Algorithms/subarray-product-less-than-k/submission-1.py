class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0

        cursum = 1
        l=0
        for r in range(len(nums)):
            cursum *= nums[r]
            while cursum>=k and l<=r:
                cursum//=nums[l]
                l+=1
            res+= r-l+1

        return res
