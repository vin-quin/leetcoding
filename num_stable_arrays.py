# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        '''
        A binary array arr is called stable if:

        The number of occurrences of 0 in arr is exactly zero.
        The number of occurrences of 1 in arr is exactly one.
        Each subarray of arr with a size greater than limit must contain both 0 and 1.
        Return the total number of stable binary arrays.

        Since the answer may be very large, return it modulo 109 + 7.
'''

def main():
    s = Solution()
    print(s.numberOfStableArrays())

if __name__ == '__main__':
    main()