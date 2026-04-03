# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def solve(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        from collections import deque

        closers = deque()

        # push all opening onto stack
        # when a closing appears, its opening should be at top of stack if it is valid
        # else invalid
        for c in s:
            match c:
                case "{":
                    closers.appendleft("}")
                    continue
                case "(":
                    closers.appendleft(")")
                    continue
                case "[":
                    closers.appendleft("]")
                    continue

            if len(closers) <= 0 or c != closers.popleft():
                return False

        return len(closers) == 0


def main():
    s = Solution()
    print(s.solve("()"))
    print(s.solve("()[]{}"))
    print(s.solve("(]"))
    print(s.solve("([)]"))
    print(s.solve("(("))

if __name__ == '__main__':
    main()