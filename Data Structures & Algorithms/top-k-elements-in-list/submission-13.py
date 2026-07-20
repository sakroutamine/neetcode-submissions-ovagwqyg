class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 1
        nums.sort()
        minheap = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                heapq.heappush(minheap,[-count,nums[i-1]])
                print([count,nums[i-1]])
                count = 1
            else:
                count+=1
        heapq.heappush(minheap,[-count,nums[-1]])
        retarr = []
        while k>0 and minheap:
            popped = heapq.heappop(minheap)
            print(popped)
            retarr.append(popped[1])
            k-=1
        return retarr

