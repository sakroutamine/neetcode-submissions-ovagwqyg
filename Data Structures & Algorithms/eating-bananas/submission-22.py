class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        while l<r: 
            count = 0
            k=(l+r)//2
            print(k)
            for i in piles:
                count += math.ceil(i/k)
            if count <= h:
                r=k
            else:
                l=k+1
        return l
