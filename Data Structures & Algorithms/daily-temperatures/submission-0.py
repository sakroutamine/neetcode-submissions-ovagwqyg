class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append([temperatures[i],i])
            else:
                print(i, stack)
                top = stack[-1]
                while len(stack)>0 and top[0] <= temperatures[i]:
                    stack.pop()
                    if stack:
                        top = stack[-1]
                if top[0] > temperatures[i]:
                    ret[i] = top[1]-i if top else 0
                stack.append([temperatures[i],i])
                print(i, stack)

        return ret