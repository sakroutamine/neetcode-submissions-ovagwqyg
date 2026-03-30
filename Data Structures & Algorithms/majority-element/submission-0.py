class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in nums:
            dic[i] +=1
            if dic[i] > len(nums)/2:
                return i
        return -1