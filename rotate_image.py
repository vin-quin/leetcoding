# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        a b c
        d e f
        g h i

        g d a
        h e b
        i f c

        Shift Right 2N+(N-1)
        [0,1,2,3,4,5,6,7,8]
        read bottom to top left to right = reversed
        '''


        
def main():
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()