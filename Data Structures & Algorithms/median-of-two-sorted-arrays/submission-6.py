class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = len(nums1)+len(nums2)
        half = tot//2 

        a,b = nums1, nums2

        if len(b) < len(a):
            a,b = b,a

        l,r = 0,len(a)-1


        while True:
            i=(l+r)//2
            j=half-i-2

            l1 = a[i] if i>=0 else float('-infinity')
            r1 = a[i+1] if i <len(a)-1 else float('infinity')
            l2 = b[j] if j>=0 else float('-infinity')
            r2 = b[j+1] if j < len(b)-1 else float('infinity')   

            if l1<=r2 and l2<=r1:
                if tot%2:
                    return min(r1,r2)
                return (max(l1,l2)+min(r1,r2))/2
            if l1>r2:
                r=i-1
            else:
                l=i+1
    
            