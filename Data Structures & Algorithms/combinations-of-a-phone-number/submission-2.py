class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        dic = {2:"abc",3:"def",4:"ghi", 5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        
        def back(i,srs):
            if digits == "":
                return []
            if len(srs) == len(digits):
                ret.append(srs)
                return 
            else:
                for j in dic[int(digits[i])]:
                    back(i+1, srs+str(j))
            
        back(0,"")
        return ret