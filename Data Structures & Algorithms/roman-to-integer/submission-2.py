class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot = 0
        i=0
        while i <len(s):
            print(s[i])
            print(tot)
            if i<len(s)-1 and ((s[i]=="I" and s[i+1] in "VX") or (s[i]=="X" and s[i+1] in "LC") or (s[i]== "C" and s[i+1] in "DM")):
                print(s[i], s[i+1])
                tot+= dic[s[i+1]]-dic[s[i]]
                i+=1
            else:
                tot+=dic[s[i]]
            i+=1
        
        return tot