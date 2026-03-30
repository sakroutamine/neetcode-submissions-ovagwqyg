class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<r:
            su=0
            k=(r+l)//2
            for i in piles:
                su+=math.ceil(i/k)
            if su<=h:
                r=k
            else:
                l=k+1
        return l

            

