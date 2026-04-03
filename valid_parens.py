# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def solve(self, s: str) -> bool:
        ...


def main():
    s = Solution()
    print(s.solve("()"))
    print(s.solve("()[]{}"))
    print(s.solve("(]"))
    print(s.solve("([)]"))

if __name__ == '__main__':
    main()