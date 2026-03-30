class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        minmax = r

        def isMax(mid):
            subarr = 1
            m=mid
            for i in nums:
                if m-i < 0:
                    subarr +=1
                    m=mid
                    print("0ed")
                m=m-i
                print(m)
            print("subarr",mid, subarr)
            return subarr

        while l<=r:
            mid=(l+r)//2
            print("mid", mid)
            numarr= isMax(mid)
            if numarr > k:
                print("moved l to mid",l,r)
                l=mid+1
            else:
                print("r to mid", l, r, numarr)
                minmax=mid
                r=mid-1
                

        return minmax
        



        # ls,rs = 0,0
        # 
        # while l<=r:
        #     m= (l+r)//2
        #     ls = sum(nums[0:m])
        #     print(nums[0:m])
        #     rs = sum(nums[m:len(nums)])
        #     print(nums[m:len(nums)])
        #     if rs == ls:
        #         return ls
        #     elif rs < ls:
        #         r=m-1
        #     else:
        #         l=m+1

        #     print(rs,ls)
        
        # return max(ls,rs)
        