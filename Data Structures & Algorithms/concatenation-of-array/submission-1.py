class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length=len(nums) 
        arr = [0] * 2 * length
        
        for i in range(length):
            arr[i] = arr[i+length] = nums[i]
        return arr