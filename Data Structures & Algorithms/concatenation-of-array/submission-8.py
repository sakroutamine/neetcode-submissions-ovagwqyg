class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)*2
        for i in range(len(nums)):
            ret[i] = ret[i+len(nums)] = nums[i]

        return ret





































        # length=len(nums) 
        # arr = [0] * 2 * length
        
        # for i in range(length):
        #     arr[i] = arr[i+length] = nums[i]
        # return arr