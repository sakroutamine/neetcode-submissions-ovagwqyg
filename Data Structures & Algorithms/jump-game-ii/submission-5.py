class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l,r = 0,0
        maxj = 0

        while r<len(nums)-1:
            print(l,r, jumps,maxj)
            maxj = max(maxj, l+nums[l])
            if l==r:
                l=r
                r=maxj
                jumps+=1
            l+=1
            
        return jumps
        