# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def solve(self,  nums: list[int], target: int) -> int:
        # If the mid point is greater than mid-1, then we are a sorted arr and can run as normal
        # Else typical binary search rules need to be reversed
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]: # The array must be sorted properly for this to hold true
            return search(nums, target, l, r)
        elif target > nums[mid]: # target will be on left
            return search(nums, target, l, mid-1)
        else: # target will be on right
            return search(nums, target, mid+1, r)
        


def search(nums: list[int], target: int, l: int, r: int) -> int:
    if l > r:
        return -1
    
    mid = l+(r-l)//2
    if nums[mid] == target:
        return mid
    
    if nums[l] < nums[mid] > target: # array gets smaller to left and our target is smaller than mid
        return search(nums, target, l, mid-1)
    else:
        return search(nums, target, mid+1, r)


def main():
    s = Solution()
    print(s.solve([4,5,6,7,0,1,2], 0), 4)
    print(s.solve([4,5,6,7,0,1,2], 3), -1)
    print(s.solve([0,1,2,3,4,5,6], 2), 2)
    print(s.solve([1], 0), -1)

if __name__ == '__main__':
    main()