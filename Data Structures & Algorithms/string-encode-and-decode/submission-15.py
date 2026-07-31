class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if strs ==[]:
            return '_'
        ret = '`'.join(strs)
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        if s=='_':
            return []
        
        return s[:len(s)].split("`")
