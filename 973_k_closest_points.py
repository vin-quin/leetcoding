# https://leetcode.com/problems/k-closest-points-to-origin/description/
from math import sqrt
import heapq 

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dists = [[sqrt((p[0])**2 + (p[1])**2), p] for p in points]

        return [v[1] for v in heapq.nsmallest(k, dists, key=lambda x: x[0])]

        # return [heapq.heappop(dists) for i in range(k)]

def main():
    s = Solution()
    print(s.kClosest([[1,3], [-2,2]], 1), [-2,2])

if __name__ == '__main__':
    main()