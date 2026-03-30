class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        arr=[] 
        dic = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        def feedback(i, curStr):
            if len(curStr) == len(digits):
                arr.append(curStr)
                return

            for c in dic[int(digits[i])]:
                feedback(i+1, curStr+c)

        if digits:
            feedback(0,"")
 
        return arr
        
