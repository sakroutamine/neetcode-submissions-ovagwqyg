class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = []

        combine = [(p,s) for p,s in zip(position,speed)]
        combine.sort(reverse=True)
        print(combine)

        for p,s in combine:
            
            tottime = (target-p)/s
            stack.append(tottime)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            print(p,s,tottime)
            
        print(stack)
        
        return len(stack)
            