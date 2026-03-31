import heapq

class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.count = 0
        self.removed = set()
        # heapq.heapify(self.heap)

    def push(self, x: int) -> None:
        self.stack.append((x,self.count * -1))
        heapq.heappush(self.heap, (-x,-self.count))
        self.count+=1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        popped = self.stack.pop()
        self.removed.add(popped[1])
        return popped[0] 

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        maxi = self.heap[0]
        while maxi[1] in self.removed:
            heapq.heappop(self.heap)
            maxi = self.heap[0]
        return maxi[0] * -1

    def popMax(self) -> int:
        maxi = self.heap[0]
        while maxi[1] in self.removed:
            heapq.heappop(self.heap)
            maxi = self.heap[0]
        self.removed.add(maxi[1])
        ret = heapq.heappop(self.heap)[0] * -1
        return ret


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
