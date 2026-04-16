# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def solve(self,  nums: list[int], target: int) -> int:
        # If the mid point is greater than mid-1, then we are a sorted arr and can run as normal
        # Else typical binary search rules need to be reversed
        l, r = 0, len(nums)-1
        return search(nums, target, l, r)

def search(nums: list[int], target: int, l: int, r: int) -> int:
    if l > r:
        return -1
    
    mid = l+(r-l)//2
    if nums[mid] == target:
        return mid
    
    if nums[l] == target:
        return l
    
    if nums[r] == target:
        return r
    
    # We dont know where true bounds are so we shimmy left and right until we can properly binary search when we find the range
    if target < nums[l]:
        return search(nums, target, l+1, r)
    elif target > nums[r]:
        return search(nums, target,l,  r-1)
    elif target > nums[mid]:
        return search(nums, target, mid+1, r)
    elif target < nums[mid]:
        return search(nums, target,l,  mid-1)

    return -1

def main():
    s = Solution()
    print(s.solve([4,5,6,7,0,1,2], 0), 4)
    print(s.solve([4,5,6,7,0,1,2], 3), -1)
    print(s.solve([0,1,2,3,4,5,6], 2), 2)
    print(s.solve([1], 0), -1)
    print(s.solve([3,5,1], 3), 0)
    print(s.solve([5,1,2,3,4], 1), 1)

if __name__ == '__main__':
    main()