# https://leetcode.com/problems/last-stone-weight/description/
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if x != y:
                y -= x
                heapq.heappush_max(stones, y)

        return stones[0] if stones else 0