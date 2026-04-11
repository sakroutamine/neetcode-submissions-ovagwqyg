class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        n=len(nums)
        prod = 1

        for i in range(1,n):
            ret[i]=ret[i-1]*nums[i-1]
        print(ret)

        for i in range(n-1,-1,-1):
            print(prod)
            ret[i]*=prod
            prod*=nums[i]
            
            
        return ret

        