class MinStack:

    def __init__(self):
        self.stack = []
        # self.minVal =  -float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.minVal = min(self.minVal, val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        # if 
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)

        
