# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def solve(self, tokens: list[str]) -> int:
        from collections import deque
        from math import trunc
        operands = deque()

        # Every time we see an operand (num), store it. This includes results from our calcs
        # When we see an operator, perform the first operation we can with the operators in the stack
        # If none obviously invalid
        for t in tokens:
            match t:
                case '*':
                    right, left = operands.pop(), operands.pop()
                    operands.append(left * right)
                case '/':
                    right, left = operands.pop(), operands.pop()
                    operands.append(trunc(left / right))
                case '+':
                    right, left = operands.pop(), operands.pop()
                    operands.append(left + right)
                case '-':
                    right, left = operands.pop(), operands.pop()
                    operands.append(left - right)
                case _:
                    operands.append(int(t))

        return operands.pop() # last element is result

def main():
    s = Solution()
    print(s.solve(["2","1","+","3","*"]))
    print(s.solve( ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

if __name__ == '__main__':
    main()