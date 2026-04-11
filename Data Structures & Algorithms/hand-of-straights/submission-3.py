class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        minheap = hand
        dic = defaultdict(int)
        for i in hand:
            dic[i]+=1
        heapq.heapify(minheap)
        size = groupSize

        while minheap:
            currval = heapq.heappop(minheap)
            print(currval)
            if dic[currval] == 0:
                continue
            while size > 0:
                print(size, currval, dic[currval])
                if dic[currval]>0:
                    dic[currval]-=1
                    size-=1
                    currval +=1
                else:
                    return False
                
            size = groupSize
        print(dic)
        return True
            

