class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()

        for i,j in intervals:
            if stack and stack[-1][1]>=i:
                stack[-1][1]=max(stack[-1][1],j)
            else:
                stack.append([i,j])

        return stack