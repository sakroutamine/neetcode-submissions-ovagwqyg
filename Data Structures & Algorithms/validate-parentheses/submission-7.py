class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','[':']','{':'}'}

        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
            else:
                if stack and dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            print(stack)
        
        return False if len(stack) > 0 else True