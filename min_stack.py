# https://leetcode.com/problems/min-stack/description/
class MinStack:
    def __init__(self):
        self.items = []
        self.mins = [] # Synced with mins, pos in mins stack is the min for current pos in items stack

    def push(self, val: int) -> None:
        self.items.append(val)

        if len(self.items) == 1:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]

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