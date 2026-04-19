class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for j,i in enumerate(nums):
            if target-i in dic:
                return [dic[target-i],j]
            dic[i]=j
        
        return 0

