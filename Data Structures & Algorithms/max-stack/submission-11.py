import heapq

class MaxStack:
    def __init__(self):
        self.stack = []
        self.heap = []
        heapq.heapify(self.heap)
        self.removed = set()
        self.counter = 0

    def push(self, x: int) -> None:
        self.stack.append((x,-self.counter))
        heapq.heappush(self.heap, (-x, -self.counter))
        self.counter +=1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
             self.stack.pop()
        popped = self.stack.pop()
        self.removed.add(popped[1])

        return popped[0]

    
    def top(self) -> int:
        if not self.stack:
            return 0
        peek = self.stack[-1]
        while peek[1] in self.removed:
            self.stack.pop()
            peek = self.stack[-1]
        
        return peek[0]

    def peekMax(self) -> int:
        peek = self.heap[0]
        while peek[1] in self.removed:
            heapq.heappop(self.heap)
            peek = self.heap[0]
        
        return peek[0] * -1

    def popMax(self) -> int:
        removed = self.heap[0]
        while removed[1] in self.removed:
            heapq.heappop(self.heap)
            removed = self.heap[0]
        self.removed.add(removed[1])
        print(removed[0])
        return removed[0] * -1

    # def popMax(self) -> int:
    #     maxi = self.heap[0]
    #     while maxi[1] in self.removed:
    #         heapq.heappop(self.heap)
    #         maxi = self.heap[0]
    #     self.removed.add(maxi[1])
    #     ret = heapq.heappop(self.heap)[0] * -1
    #     return ret


    # def __init__(self):
    #     self.stack = []
    #     self.heap = []
    #     self.count = 0
    #     self.removed = set()
    #     # heapq.heapify(self.heap)

    # def push(self, x: int) -> None:
    #     self.stack.append((x,self.count * -1))
    #     heapq.heappush(self.heap, (-x,-self.count))
    #     self.count+=1

    # def pop(self) -> int:
    #     while self.stack and self.stack[-1][1] in self.removed:
    #         self.stack.pop()
    #     popped = self.stack.pop()
    #     self.removed.add(popped[1])
    #     return popped[0] 

    # def top(self) -> int:
    #     while self.stack and self.stack[-1][1] in self.removed:
    #         self.stack.pop()
    #     return self.stack[-1][0]
        
    # def peekMax(self) -> int:
    #     maxi = self.heap[0]
    #     while maxi[1] in self.removed:
    #         heapq.heappop(self.heap)
    #         maxi = self.heap[0]
    #     return maxi[0] * -1

    # def popMax(self) -> int:
    #     maxi = self.heap[0]
    #     while maxi[1] in self.removed:
    #         heapq.heappop(self.heap)
    #         maxi = self.heap[0]
    #     self.removed.add(maxi[1])
    #     ret = heapq.heappop(self.heap)[0] * -1
    #     return ret


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
