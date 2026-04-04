# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def solve(self, tokens: list[str]) -> int:
        ...


def main():
    s = Solution()
    print(s.solve(["2","1","+","3","*"]))

if __name__ == '__main__':
    main()