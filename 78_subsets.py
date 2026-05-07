# https://leetcode.com/problems/subsets/description/
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        backtrack(nums, 0, [], subsets)

        return subsets
        
def backtrack(nums: list[int], i: int, thisSet: list[int], subsets: list[list[int]]):
    if i >= len(nums):
        subsets.append([*thisSet])
        return
    
    thisSet.append(nums[i])
    backtrack(nums, i+1, thisSet, subsets)
    thisSet.pop()

    backtrack(nums, i+1, thisSet, subsets)


def main():
    s = Solution()
    print(s.solve([1,2,3]))

if __name__ == '__main__':
    main()