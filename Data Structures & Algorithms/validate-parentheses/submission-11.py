class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','[':']','{':'}'}
        stack = []

        for i in s:
            if i == '(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack and i == dic[stack[-1]]:
                    print(stack[-1])
                    stack.pop()
                else:
                    return False

        print(stack)
        return len(stack) == 0