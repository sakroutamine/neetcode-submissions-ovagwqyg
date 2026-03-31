class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            if maxHeap[0] == maxHeap[1]:
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
            elif maxHeap[0] < maxHeap[1]:
                y = heapq.heappop(maxHeap)
                x = heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,y-x)
        if len(maxHeap) == 0:
            return 0
        return maxHeap[0] * -1