class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        
        for i in intervals:
            l,r = 0,0
            print(i)
            if stack and stack[-1][1]>=i[0]:
                print("inside")
                l=min(stack[-1][0], i[0])
                r = max(stack[-1][1], i[1])
                stack.pop()
                stack.append([l,r])
            else:
                print("else", stack)
                stack.append(i)
        return stack
