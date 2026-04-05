class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(arr)-k
        ret = []

        while l<r:
            print(l,r)
            m=(l+r)//2
            a = arr[m]
            b = arr[m+k]
            print((abs(a-x), abs(b-x)))
            if abs(a-x) < abs(b-x) or (abs(a-x) == abs(b-x) and a < b):
                r=m
            else:
                l=m+1
            print(l,r)
                

        return arr[l:l+k]
        # while l<r:
        #     m=(l+r)//2
        #     if arr[m] == x or l+1==r:
        #         break
        #     elif arr[m] > x:
        #           r=m-1
        #     else:
        #         l=m

        # while k >0:
        #     print(l,r)
        #     print(arr)
        #     if abs(arr[l]-x) < abs(arr[r]-x) or (abs(arr[l]-x) == abs(arr[r]-x) and arr[l]<arr[r]):
        #         ret.append(arr.pop(l))
        #         l-=1
        #     else:
        #         ret.append(arr.pop(r))
        #     r-=1
        #     k-=1
        #     print(arr)

        # return sorted(ret)