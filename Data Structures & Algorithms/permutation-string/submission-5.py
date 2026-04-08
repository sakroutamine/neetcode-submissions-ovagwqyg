class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1arr = [0] * 26
        s2arr = [0] * 26
        for i in range(len(s1)):
            s1arr[ord(s1[i])-ord('a')] +=1
            s2arr[ord(s2[i])-ord('a')] +=1
        
        print(s1arr)
        l = 0
        if s1arr == s2arr:
                return True
        for r in range(len(s1),len(s2)):
            print(s2[l],s2[r],s2arr)
            if s1arr == s2arr:
                return True
            s2arr[ord(s2[l])-ord('a')] -=1
            s2arr[ord(s2[r])-ord('a')] +=1
            l+=1
        if s1arr == s2arr:
                return True    

        return False

            
        

        
            

        return False