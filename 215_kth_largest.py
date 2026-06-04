# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq 

class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


def main():
    s = Solution()
    print(s.solve([3,2,1,5,6,4], 2))

if __name__ == '__main__':
    main()