class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for x,i in enumerate(nums):
            
            if target-i in dic:
                return [dic[target-i], x]
            dic[i] = x

        return []