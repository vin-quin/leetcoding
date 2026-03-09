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

        z=1,o=2,l=1
        [1,1,0]
        [1,1]=F
        [1,0]=T
            [1,0,1]=T
            [1,0,0]=F

        Result is 1

        z=3,o=3,l=2
        [1,1,1,0,0,0]
        [1,1,1]=F
        [1,1,0]=T
            [1,1,1,0]=T
            [1,1,0,0]=T
            [1,0,0,0]=T
                [1,1,1,0,0]=T
                [1,1,0,0,0]=T
                    [1,1,1,0,0,0]=T

        Result is 14, just double if array length is even since it can be mirrored?

        Build such that we always create a valid subarr
    '''
        
        arr = [1] * one + [0] * zero
        print(arr)
        
        subarrs = [arr[i:i+limit+1] for i in range(len(arr) - limit)]
        print(subarrs)

        stable = 0
        for a in subarrs:
            if 0 in a and 1 in a:
                print(f'Subarr: {a} is stable')
                stable += 1

        print(f'{stable=}')
        num_stable = 0
        for i in range(1, stable+1):
            num_stable += 2 ** i
        print(f'num_stable: {num_stable}')
            

def main():
    s = Solution()
    print(s.numberOfStableArrays(1,2,1))
    print(s.numberOfStableArrays(3,3,2))
    print(s.numberOfStableArrays(1,1,2))

if __name__ == '__main__':
    main()