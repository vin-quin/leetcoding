# https://leetcode.com/problems/k-closest-points-to-origin/description/
# 
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ...


def main():
    s = Solution()
    print(s.kClosest([[1,3], [-2,2]], 1), [-2,2])

if __name__ == '__main__':
    main()