class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        arr=[] 
        dic = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        def feedback(i, car):
            if len(car) == len(digits):
                arr.append(car)
                return
            
            for j in dic[int(digits[i])]:
                feedback(i+1, car+j)

            
        if digits:
            feedback(0,"")
        return arr
        
