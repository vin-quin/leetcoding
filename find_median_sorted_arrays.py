# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...


def main():
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]), 2.00000)
    print(s.findMedianSortedArrays([1,2], [3,4]), 2.50000)

if __name__ == '__main__':
    main()