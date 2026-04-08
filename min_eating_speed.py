# https://neetcode.io/problems/eating-bananas/question?list=neetcode150
class Solution:
    def solve(self, piles: list[int], h: int) -> int:
        # Can only eat from one pile at a time
        [24,18,11,0]
        [0,3,9,16]

        remaining = [0] * len(piles)
        for i in range(len(piles)-2, -1, -1):
            remaining[i] = remaining[i+1] + piles[i+1]

        print(remaining)
        speed = piles[0]
        print(speed*(h-1))
        while (speed * (h-1)) < remaining[0]:
            speed += 1

        return speed


def main():
    s = Solution()
    print(s.solve([3,6,7,11], 8))
    print(s.solve([30,11,23,4,20], 5))
    print(s.solve([30,11,23,4,20], 6))

if __name__ == '__main__':
    main()