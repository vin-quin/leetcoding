# https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150
class Solution:
    def solve(self, grid: list[list[int]]) -> None:
        ...


def main():
    s = Solution()
    print(s.solve([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]))

if __name__ == '__main__':
    main()