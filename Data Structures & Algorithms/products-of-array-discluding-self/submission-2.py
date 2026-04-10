class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lent = len(nums)
        ret = [1] * lent
        post = 1

        for i in range(1,lent):
            ret[i] *= ret[i-1] * nums[i-1]
        for j in range(lent-1,-1,-1):
            ret[j] *= post
            post *= nums[j]


        return ret