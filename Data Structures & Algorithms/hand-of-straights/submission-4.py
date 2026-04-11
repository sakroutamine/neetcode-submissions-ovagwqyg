class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic = defaultdict(int)
        for i in hand:
            dic[i]+=1
        minheap = hand
        heapq.heapify(minheap)
        size = groupSize
        while minheap:

            popped = heapq.heappop(minheap)
            if dic[popped] == 0:
                continue
            print(popped, dic)
            while size>0:
                
                if dic[popped]==0:
                    return False
                dic[popped]-=1
                popped+=1
                size-=1
            size = groupSize
        return True

