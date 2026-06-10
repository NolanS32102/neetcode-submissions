class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) != 0:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val) 

    def pop(self) -> None:
        if len(self.stack) != 0:
            top = self.stack[-1]
            minTop = self.minStack[-1]
            if top == minTop:
                self.minStack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
