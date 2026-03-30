class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<r:
            su=0
            k=(r+l)//2
            print("rep",k, su)
            for i in piles:
                su+=math.ceil(i/k)
                print(su)
            if su<=h:
                res=min(res,k)
                print(res)
                r=k
            else:
                l=k+1
        return res

            

