class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for i in strs:
            ret+= str(len(i))+"*"+i
        
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        tmp = ""
        i = 0
        while i < len(s):
            if s[i] == "*":
                ret.append(s[i+1:i+1+int(tmp)])
                i+= int(tmp)
                tmp = ""
            else:
                tmp=tmp+s[i]
            i+=1
        return ret