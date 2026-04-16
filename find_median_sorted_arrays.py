# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # If len of a + b is odd we have a true median
        # If even we must calculate the median
        # [1,2,3], [4,5]

        # [1,6,9], [4,5] -> [1,4,5,6,9] -> 5
        
        combined = nums1

        for n in nums2:
            if n >= combined[-1]: 
                combined.append(n)
                continue
            # ins = bisect_left(combined, n, 0, len(combined)-1)
            ins = bisect.bisect_left(combined, n, 0, len(combined)-1)
            combined.insert(ins, n)

        mid = len(combined)//2
        if len(combined) % 2 == 0: 
            return (combined[mid] + combined[mid-1]) / 2

        return combined[mid]

def bisect_left(nums: list[int], target: int, l: int, r: int):
    if r < l:
        return l-1
    
    mid =l+(r-l)//2
    if nums[mid] == target:
        return mid-1
    
    if nums[mid] <= target:
        return bisect_left(nums, target, l, mid-1)
    else:
        return bisect_left(nums, target, mid+1, r)

def main():
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]), 2.00000)
    print(s.findMedianSortedArrays([1,2], [3,4]), 2.50000)
    print(s.findMedianSortedArrays([1,6,9], [4,5]), 5.00000)

if __name__ == '__main__':
    main()