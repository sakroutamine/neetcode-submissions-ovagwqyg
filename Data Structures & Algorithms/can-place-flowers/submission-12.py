class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeroes=1 if not flowerbed[0] else 0
        for i in flowerbed:
            if i:
                n-= int((zeroes-1) /2)
                zeroes = 0
            else:
                zeroes +=1


        n-= int(zeroes / 2)

        return n <=0
