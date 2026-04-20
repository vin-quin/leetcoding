# https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        ...


def main():
    s = Solution()
    print(s.solve([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

if __name__ == '__main__':
    main()