class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0 or val < self.mins[-1]:
            self.mins.append(val) 
        else:
            self.mins.append(self.mins[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

'''
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

stack = []
mins = []

stack = [-2]
mins = [-2]

stack = [-2,0]
mins = [-2,-2]

stack = [-2,0,-3]
mins = [-2,-2,-3]

stack = [-2,0]
mins = [-2,-2]

stack = [-2,0]
mins = [-2,-2]
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()