# https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []

        '''
        0, 0..n
        0..n, n-1
        n-1,n..0

        R,D,L 2x2
        R,R,D,D,L,L,U,R 3x3
        R,R,R,D,D,L,L,L,U,R,R 4x3
        R,R,R,D,D,D,L,L,L,U,U,R,R,D,L 4x4

        Always (N*M)-1 moves as we start at 0,0
        '''

        idx = 0
        n, m = len(matrix), len(matrix[0])
        while idx < n * m:
            x, y = to2D(idx, n, m)
            spiral.append(matrix[y][x])
            idx += 1

        return spiral

def to2D(idx, n, m):
    x = idx % n
    y = idx % m + (idx // m)
    return x, y

def main():
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()