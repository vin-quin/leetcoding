# https://neetcode.io/problems/eating-bananas/question?list=neetcode150
class Solution:
    def solve(self, piles: list[int], h: int) -> int:
        # Can only eat from one pile at a time
        piles.sort()

        if len(piles) == h: # Gotta eat as fast as possible
            return piles[-1]
        
        # Start with median as eatSpeed
        # Every hour we remove eatSpeed from a pile
        # If we have eaten all piles before time is up, save this as bestEatSpeed
        #   Then halve it and repeat
        # If we ran out of time before finishing all piles
        #   Add half length to eatSpeed then repeat
        # If we have eaten everything and used all time, then we are done
        
        # Remove speed from a spot every hour we will get an answer O(N)
        for hour in h: 


        return 0


def main():
    s = Solution()
    print(s.solve([3,6,7,11], 8))
    print(s.solve([30,11,23,4,20], 5))
    print(s.solve([30,11,23,4,20], 6))

if __name__ == '__main__':
    main()