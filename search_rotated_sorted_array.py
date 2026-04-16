# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def solve(self,  nums: list[int], target: int) -> int:
        # If the mid point is greater than mid-1, then we are a sorted arr and can run as normal
        # Else typical binary search rules need to be reversed
        
        l, r = 0, len(nums)-1
        # if nums[l] < nums[r]: # The array must be sorted properly for this to hold true
        return search(nums, target, l, r)
        # elif target > nums[mid]: # target will be on left
        #     return search(nums, target, l, mid-1)
        # else: # target will be on right
        #     return search(nums, target, mid+1, r)
        
# if left < mid < target then I must go right

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
    
    if nums[l] <= nums[mid] <= nums[r]: # This section is properly sorted
        if nums[mid] > target:
            return search(nums, target, l, mid-1)
        else:
            return search(nums, target, mid+1, r)
    else: # We are not properly sorted so invert the typical rules
        if nums[mid] < nums[min(mid+1, r)]: # The next num is greater, normal binary search

        
        if target <= nums[r]: # target is smaller than midpoint, go right instead
            return search(nums, target, mid+1, r)
        else:
            return search(nums, target, l, mid-1)
78123456
# If target LESS than LEFT then it must be on the right side
# Elif target GREATER than RIGHT it must be on the left side
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