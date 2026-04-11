class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        lent = len(nums1)+len(nums2)
        half= lent//2
        a,b = nums1,nums2

        if len(a) > len(b):
            b,a, = a,b


        l,r = 0, len(a)-1
        while True:
            i=(l+r)//2
            if l > r:
                i = -1
            j=half-i-2

            l1=a[i] if i>=0 else float('-inf')
            r1=a[i+1] if i+1<len(a) else float('inf')
            l2=b[j] if j>=0 else float('-inf')
            r2=b[j+1]  if j+1<len(b) else float('inf')


            if l1 <= r2 and l2 <=r1:

                if lent % 2:
                    return min(r1, r2)
                return (max(l1,l2)+min(r1,r2))/2

            elif l1 > r2:
                r=i-1
            else:
                l=i+1

        return False

            


        

        return ()/2.0