# https://leetcode.com/problems/min-stack/description/
class MinStack:
    def __init__(self):
        self.items = []
        self.min = -1

    def push(self, val: int) -> None:
        self.items = [val] + self.items
        self.min += 1

        if self.items[self.min] > val:
            self.min = 0 # new top of stack is min

    def pop(self) -> None:
        self.items.pop(0)
        if self.min == 0:
            self.min = self.items.index(min(self.items))
        else:
            self.min -= 1
        

    def top(self) -> int:
        return self.items[0]

    def getMin(self) -> int:
        return self.items[self.min]

    def __str__(self):
        return f'{self.items=}/{self.min=}'
    
    def __repr__(self):
        return f'{self.items=}/{self.min=}'
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack)
    minStack.getMin() 
    minStack.pop()
    minStack.top()    
    minStack.getMin() 

if __name__ == '__main__':
    main()