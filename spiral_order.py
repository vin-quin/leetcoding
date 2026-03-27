# https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []

        '''
        0, 0..n
        0..n, n-1
        n-1,n..0

        0,1,2
        3,4,5
        6,7,8
        
        0,  1,  2,  3,  4
        5,  6,  7,  8,  9
        10, 11, 12, 13, 14
        15, 16, 17, 18, 19
        20, 21, 22, 23, 24

        R,D,L 2x2
        R,R,D,D,L,L,U,R 3x3
        R,R,R,D,D,L,L,L,U,R,R 4x3
        R,R,R,D,D,D,L,L,L,U,U,R,R,D,L 4x4

        For N=5,M=5
        N-1 R
        M-1 D
        N-1 L
        M-2 U
        N-2 R
        M-3 D
        N-3 L
        M-4 U
        N-4 R

        Always (N*M)-1 moves as we start at 0,0
        '''

        solve(matrix, spiral)

        return spiral

def solve(matrix, spiral):
    if len(matrix) == 0 or len(matrix[0]) == 0: # Done 
        return 
    
    r, c = len(matrix), len(matrix[0])
    print(f'{c=},{r=}')
    print(f'{matrix=}')

    if r==1:
        spiral += [*matrix[0]]
        return
    
    if c==1:
        for i in range(r):
            spiral.append(matrix[i][0])
        return

    # if c*r == 1:
    #     spiral.append(matrix[0][0])
    #     return 
    
    # if c*r == 2:
    #     spiral.append(matrix[0][0])
    #     spiral.append(matrix[r-1][c-1])
    #     return
    
    for i in range(c): # R
        print('R')
        spiral.append(matrix[0][i])
    
    for i in range(1, r): # D, Skip top right
        print('D')
        spiral.append(matrix[i][-1])
    
    for i in range(c-2, 0, -1): # L, Skip bottom right
        print('L')
        spiral.append(matrix[-1][i])

    for i in range(r-1, 0, -1): # U, Skip bottom left
        print('U')
        spiral.append(matrix[i][0])

    # Call again on subarr
    solve([ matrix[row][1:-1] for row in range(1,r-1) ], spiral)
    
def main():
    s = Solution()
    # print(s.spiralOrder([[3], [2]]))
    # print(s.spiralOrder([[6,9,7]]))
    # print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    # print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))

if __name__ == '__main__':
    main()