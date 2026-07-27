class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)

def main():
    s = Solution()
    print(s.minMoves([1,2,3]))
    print(s.minMoves([-1,1,1]))

if __name__ == '__main__':
    main()