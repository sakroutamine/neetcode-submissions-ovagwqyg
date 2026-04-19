class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{":"}","[":"]","(":")"}
        stack = []
        
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif stack and i==dic[stack[-1]]:
                stack.pop()
            else:
                return False
        

        return len(stack)==0


            