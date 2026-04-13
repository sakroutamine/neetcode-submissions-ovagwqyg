class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]<1:
                nums[i] = n+1
        print(nums)
        for j in range(n):
            if abs(nums[j])<=n and nums[abs(nums[j])-1]>0:
                nums[abs(nums[j])-1] *=-1

        print(nums)    
        for k in range(n):
            if nums[k]>0:
                return k+1

        return n+1