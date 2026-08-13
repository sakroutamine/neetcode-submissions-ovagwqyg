class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        

        while i<j:
            while not str.isalnum(s[i]) and i<len(s)-1 and i<j:
                print(i)
                i+=1
            while not str.isalnum(s[j]) and j >0 and j>i:
                print('j',j)
                j-=1
            print(s[i], s[j])
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
                
            

        return True