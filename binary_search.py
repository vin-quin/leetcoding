# https://leetcode.com/problems/binary-search/description/
class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        return bsearch(nums, target, 0, len(nums)-1)

def bsearch(nums: list[int], target: int, l :int, r: int) -> int:
    if l > r:
        return -1
    
    mid = l + ((r-l) // 2)
    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return bsearch(nums, target, l, mid-1)
    elif target > nums[mid]:
        return bsearch(nums, target, mid+1, r)


def main():
    s = Solution()
    print(s.solve([-1,0,3,5,9,12], 9))
    print(s.solve([-1,0,3,5,9,12], 2))
    print(s.solve([-1,0,2,4,6,8], 4))
    print(s.solve([-1,0,2,4,6,8], 3))
    print(s.solve([3], 3))
    print(s.solve([1], 3))
    print(s.solve([-1,0,3,5,9,12], 13))

if __name__ == '__main__':
    main()