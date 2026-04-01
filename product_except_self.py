# https://neetcode.io/problems/products-of-array-discluding-self/question?list=blind75
class Solution:
    def solve(self, nums: list[int]) -> list[int]:
        # Every time we pick i it is bisects nums into 2
        prefixes = [1] * len(nums) # Every product up to i

        for i in range(1, len(nums)):
            prefixes[i] = nums[i-1] * prefixes[i-1]

        print(prefixes)
        
        suffixes = [1] * len(nums) # Every product up to i

        for i in range(len(nums)-2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]

        print(suffixes)

        prods = [prefixes[i] * suffixes[i] for i in range(len(nums))]

        return prods



def main():
    s = Solution()
    print(s.solve([1,2,3,4]))
    # print(s.solve([1,2,4,6]))

if __name__ == '__main__':
    main()