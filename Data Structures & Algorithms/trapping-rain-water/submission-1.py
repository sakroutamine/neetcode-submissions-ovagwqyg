class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxl,maxr =0,0
        totwater = 0

        while l<r:
            print(l,r)
            if height[l] <= height[r]:

                if maxl-height[l]>0:
                    print("l",l, totwater, maxl)
                    totwater+=maxl-height[l]

                maxl = max(maxl, height[l])
                l+=1
            else:
                if maxr-height[r]>0:
                    print("r", r, totwater, maxl)
                    totwater+=maxr-height[r]

                maxr = max(maxr, height[r])
                r-=1
        return totwater

