class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        count = Counter(tasks)
        q=deque()
        print(count)
        maxHeap = [-n for n in count.values()]
        heapq.heapify(maxHeap)
        
        print(maxHeap, count)
        while maxHeap or q:
            cycles+=1
            
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,cycles+n])
            
            if q and q[0][1] == cycles:
                heapq.heappush(maxHeap, q.popleft()[0])
            

        return cycles