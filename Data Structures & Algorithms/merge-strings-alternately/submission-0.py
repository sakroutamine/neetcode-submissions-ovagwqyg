class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st = ""
        p1,p2 = 0,0

        while p1 != len(word1) and p2 != len(word2):
            st+=word1[p1]
            st+=word2[p2]
            p1+=1
            p2+=1
        

        if p1==len(word1) and p2<len(word2):
            st+=word2[p2:]
        if p1<len(word1) and p2==len(word2):
            st+=word1[p1:]

        return st

