# https://neetcode.io/problems/eating-bananas/question?list=neetcode150
class Solution:
    def solve(self, piles: list[int], h: int) -> int:
        # Can only eat from one pile at a time
        # What is the smallest number of bananas I can eat that makes all piles 0 by time h

        piles.sort()

        # Koko eats h times (so she eats as slow as possible)
        # If h == number of piles, Koko must eat at the max pile size to finish in time
        if len(piles) == h:
            return piles[-1]
        
        # k = eatingSpeed
        # Starting at k=maxEatingSpeed, we can binary search with different k's to determine the optimal
        # rate faster than searching every value from k up/down
        k = piles[-1]
        consumptionTime = 0

        from math import ceil
        while consumptionTime != h: # O(log h)
            print(f'Trying consumption with {k=}')
            consumptionTimes = [ceil(v/k) for v in piles] # O(N)
            
            print(consumptionTimes)

            consumptionTime = sum(consumptionTimes)
            print(consumptionTime)

            if consumptionTime < h: # Need to eat slower
                k -= k//2
            elif consumptionTime > h: # Need to eat faster
                k += k//2


        '''
        k=11
        sum(1,1,1,1) -> all consumed at h=4 for k=11

        if k is too fast:
            k -= k//2
        else if k is too slow
            k += k//2

        k=11-5=6
        sum(1,1,2,2) -> consumed @ h=6 too fast

        k=6-3=3
        sum(1,2,3,4) -> consumed @ h=10 too slow

        k=3+1
        sum(1,2,2,3) -> consumed @ h=8 perfect

        we're done
        '''


        return k


def main():
    s = Solution()
    print(s.solve([3,6,7,11], 8), 4)
    print(s.solve([30,11,23,4,20], 5), 30)
    print(s.solve([30,11,23,4,20], 6), 23)

if __name__ == '__main__':
    main()