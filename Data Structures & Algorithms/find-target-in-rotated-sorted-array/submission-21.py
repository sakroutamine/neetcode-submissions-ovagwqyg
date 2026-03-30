class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums)-1


        while l <r:
            # if nums[l] < nums[r]:
            # print(nums[l])
            m = (l+r)//2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m
        mi=l
        
        if target >= nums[mi] and target <= nums[-1]:
            l, r = mi,len(nums)-1
        else:
            l, r = 0,mi-1


        while l<=r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r=m-1
        

        return -1