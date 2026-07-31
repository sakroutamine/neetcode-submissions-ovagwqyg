class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret += i+"*/"
        
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        word = ""
        i = 0
        while i <len(s):
            if s[i] == "*" and s[i+1] == "/":
                ret.append(word)
                word = ""
                i+=1
            else:
                word += s[i]
            i+=1
        return ret
