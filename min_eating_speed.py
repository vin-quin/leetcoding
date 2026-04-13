# https://neetcode.io/problems/eating-bananas/question?list=neetcode150
class Solution:
    def solve(self, piles: list[int], h: int) -> int:
        # Can only eat from one pile at a time
        # What is the smallest number of bananas I can eat that makes all piles 0 by time h

        # # Koko eats h times (so she eats as slow as possible)
        # # If h == number of piles, Koko must eat at the max pile size to finish in time
        consumptionTime = 0
        ub, lb = max(piles), 1 # exclusive max/min k

        from math import ceil
        while lb <= ub: # O(log h)
            mid = (ub+lb)//2
            consumptionTime = sum([ceil(v/mid) for v in piles]) # O(N)

            if consumptionTime <= h: # Too fast, Need to eat slower
                ub = mid-1
            elif consumptionTime > h: # Too slow, Need to eat faster
                lb = mid+1

        return lb


def main():
    s = Solution()
    print(s.solve([3,6,7,11], 8), 4)
    print(s.solve([30,11,23,4,20], 5), 30)
    print(s.solve([30,11,23,4,20], 6), 23)
    print(s.solve([30,1,1,1,1], 6), 15)

if __name__ == '__main__':
    main()