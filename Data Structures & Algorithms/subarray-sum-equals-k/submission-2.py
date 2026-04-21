class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {0:1}
        presum = 0
        for i in nums:
            presum +=i
            if presum-k ==0 or presum-k in dic:
                count+=dic[presum-k]
            dic[presum]=dic.get(presum,0)+1

        return count
            
