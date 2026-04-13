class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i in range(len(heights)):
            earliest = i
            while stack and stack[-1][0]>heights[i]:
                popped = stack.pop()
                print(maxarea, i, popped[1], popped[0])
                maxarea = max(maxarea, (i-popped[1])*popped[0])
                earliest = min(i,popped[1])
            stack.append((heights[i],earliest))

        while stack:
            popped = stack.pop()
            print(maxarea, popped[1], popped[0])
            maxarea = max(maxarea, (len(heights)-popped[1])*popped[0])

        return maxarea