# https://leetcode.com/problems/binary-search/description/
class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        r = bsearch(nums, target)
        return r if r>=0 else -1

def bsearch(nums: list[int], target: int) -> int:
    mid = len(nums) // 2
    # print(nums, mid)
    if len(nums) == 0:
        return -1

    if nums[mid] == target:
        return mid
    
    if target < nums[mid]:
        return bsearch(nums[:mid], target)
    elif target > nums[mid]:
        return mid+bsearch(nums[mid:], target)


def main():
    s = Solution()
    # print(s.solve([-1,0,3,5,9,12], 9))
    print(s.solve([-1,0,3,5,9,12], 2))
    # print(s.solve([-1,0,2,4,6,8], 4))
    # print(s.solve([-1,0,2,4,6,8], 3))

if __name__ == '__main__':
    main()