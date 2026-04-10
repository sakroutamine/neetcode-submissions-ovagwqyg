class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = 0
        curr={5:0,10:0,20:0}

        for i in bills:
            print(i, curr)
            curr[i] +=1
            i-=5
            print(i, curr)
            while i>0:
                if i>=20 and curr[20]>0:
                    i-=20
                    curr[20]-=1
                elif i>=10 and curr[10]>0:
                    i-=10
                    curr[10]-=1
                elif i>=5 and curr[5]>0:
                    i-=5
                    curr[5]-=1
                else:
                    return False
            print(i, curr)
            if curr[5]<0 or curr[10]<0 or curr[20]<0:
                return False
            

        
        return True