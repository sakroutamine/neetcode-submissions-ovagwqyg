class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{":"}","(":")","[":"]"}
        stack = []

        for i in s:
            if not stack and i not in dic.keys():
                return False
            if i in "{([":
                stack.append(i)
            elif stack and dic[stack[-1]] == i:
                stack.pop()
            else:
                return False

        return len(stack) == 0 