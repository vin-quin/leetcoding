# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def solve(self, nums: list[int]) -> int:
        # Rotating is shifting back element to the front of the arr
        # Rotating an arr by its length does nothing

        # Pick a midpoint and use it as the current min
        # Check left and right, we will traverse whichever side is smaller.
        # If neither side is smaller, the middle MUST be the min in the array
        # Repeat

        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        print(f'LEFT [0,{mid-1}]')
        leftMin = findMin(nums[:mid], 0, mid-1)
        print(f'RIGHT [{mid},{len(nums)-1}]')
        rightMin = findMin(nums[mid:], 0, mid) + mid # Right side has mid-indexed when returning
        print(f'{leftMin=},{nums[leftMin]}')
        print(f'{rightMin=},{nums[rightMin]}')
        return min(nums[leftMin], nums[rightMin])

def findMin(nums: list[int], l: int, r: int) -> int:
    # print(f'{nums=}, {l=}, {r=}')
    if r < l:
        return -1
    
    mid = (r-l) // 2
    # print(f'{mid=}')

    if mid-1 >= 0 and nums[mid-1] < nums[mid]: # Left is smaller than current, we go
        return findMin(nums, l, mid-1)
    elif mid+1 < len(nums) and nums[mid+1] < nums[mid]: # Right is smaller than current, we go
        return findMin(nums, mid+1, r)
    else: # Both sides are greater, we must be at the min 
        return mid
        
    

def main():
    s = Solution()
    print(s.solve([3,4,5,1,2]))
    print(s.solve([4,5,6,7,0,1,2]))
    print(s.solve([11,13,15,17]))
    print(s.solve([-2]))
    print(s.solve([-2,0]))
    print(s.solve([0,-2]))

if __name__ == '__main__':
    main()