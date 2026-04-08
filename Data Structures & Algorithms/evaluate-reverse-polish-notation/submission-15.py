class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num1,num2 = -1,-1
        stack = []


        for i in tokens:
            print(stack)
            if i == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif i == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif i == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif i == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(float(num1)/num2))
            else:
                stack.append(int(i))
            

        return int(stack[0])