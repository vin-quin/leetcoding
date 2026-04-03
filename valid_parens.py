# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def solve(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        from collections import deque
        MAPPING = {
            "{": "}",
            "[": "]",
            "(": ")",
            }
        
        stack = deque()

        # push all opening onto stack
        # when a closing appears, its opening should be at top of stack if it is valid
        # else invalid
        for c in s:
            if c in MAPPING.keys():
                stack.appendleft(c)
            elif len(stack) > 0:
                opener = stack.popleft()
                if c != MAPPING[opener]:
                    return False
            else: # Stack should not be empty
                return False 

        return len(stack) == 0


def main():
    s = Solution()
    print(s.solve("()"))
    print(s.solve("()[]{}"))
    print(s.solve("(]"))
    print(s.solve("([)]"))
    print(s.solve("(("))

if __name__ == '__main__':
    main()