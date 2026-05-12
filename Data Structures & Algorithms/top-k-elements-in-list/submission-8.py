class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        ret = [] 
        nums.sort()
        print(nums)
        count = 1
        for i,x in enumerate(nums):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                count+=1
            else: 
                print(-count,nums[i])
                heapq.heappush(minheap,[-count,nums[i]])
                count = 1
        
        while k>0:
            
            popped = heapq.heappop(minheap)
            ret.append(popped[1])
            k-=1
        
        return ret

