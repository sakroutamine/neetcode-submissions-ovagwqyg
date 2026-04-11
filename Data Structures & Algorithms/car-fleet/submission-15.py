class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars=[(position[i],speed[i]) for i in range(len(position)) ]
        cars=sorted(cars)

        for i in range(len(cars)-1,-1,-1):
            time = (target-cars[i][0])/cars[i][1]
            # print(stack, time)
            if (stack and stack[-1]<time) or not stack:
                stack.append(time)
                

        return len(stack)
