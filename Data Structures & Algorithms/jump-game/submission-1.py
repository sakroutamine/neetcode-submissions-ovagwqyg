class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checkpoint=len(nums)-1
            
        for i in range(checkpoint,-1,-1):
            print(i, checkpoint)
            if i+nums[i] >= checkpoint:
                checkpoint = i
            if checkpoint<=0:
                return True
        return False
            



