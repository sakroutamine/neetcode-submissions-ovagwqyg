class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        i = 0
        if target > nums[r]:
            return r+1
        elif target < nums[l]:
            return l
        while l<=r:
            m = (r+l) // 2
            print(i,': ',m,"L ",l,"R ",r)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r=m-1
            else:
                l=m+1
        return l
