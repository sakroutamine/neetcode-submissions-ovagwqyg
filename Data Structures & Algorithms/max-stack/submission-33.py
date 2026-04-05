import heapq

class MaxStack:

    def __init__(self):
        self.stack=[]
        self.heap=[]
        self.removed = set()
        self.count = 0
        

    def push(self, x: int) -> None:
        self.stack.append((x,-self.count))
        heapq.heappush(self.heap,(-x,-self.count))
        self.count+=1
        # print(self.stack, self.heap)

    def pop(self) -> int:
        # print("pop", self.stack, self.heap)
        popped = self.stack.pop()
        while popped[1] in self.removed:
            popped = self.stack.pop()
        self.removed.add(popped[1])
        # print("pop", self.stack, self.heap)
        return popped[0]

    def top(self) -> int:
        # print("top",self.stack, self.heap)
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        # print("top",self.stack, self.heap)
        return self.stack[-1][0] if self.stack else 0    


    def peekMax(self) -> int:
        # print("pop", self.stack, self.heap)
        # top = self.heap[0]
        # while self.heap and top[1] in self.removed:
        #     heapq.heappop(self.heap)
        #     top = self.heap[0]
        # print("pop", self.stack, self.heap)
        # return top[0] * -1 
        while self.heap and self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:

        popped = self.heap[0]
        heapq.heappop(self.heap)
        while self.heap and popped[1] in self.removed:
            popped = heapq.heappop(self.heap)
        self.removed.add(popped[1])
        return popped[0] * -1
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
