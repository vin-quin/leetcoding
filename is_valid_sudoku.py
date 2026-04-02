# https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def solve(self, board: list[list[str]]) -> bool:
        '''
        Each digit in a row can only appear once (1-9)
        Each digit in a column can only appear once (1-9)
        Each digit in 3x3 subgrid can only appear once (1-9)
        '''
        for i in range(len(board)):
            seenRow = set()
            seenCol = set()
            for j in range(len(board[i])):             
                if board[i][j] != '.':
                    if board[i][j] in seenRow: # Duplicate num in row
                        return False
                    seenRow.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in seenCol: # Duplcate num in col
                        return False
                    seenCol.add(board[j][i])
                
        SUBGRID_N=3
        for i in range(SUBGRID_N):
            subgrids = {0: set(), 1: set(), 2: set()}

            for row in range(i*SUBGRID_N, (i+1)*SUBGRID_N): 
                for col in range(len(board)):
                    if board[row][col] == '.':
                        continue

                    k = col // SUBGRID_N

                    if board[row][col] in subgrids[k]: # Duplicate in 3x3
                        return False 
                    
                    subgrids[k].add(board[row][col])

        return True


def main():
    s = Solution()
#     print(s.solve([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))
    
    print(s.solve([
     [".","8","7","6","5","4","3","2","1"]
    ,["2",".",".",".",".",".",".",".","."]
    ,["3",".",".",".",".",".",".",".","."]
    ,["4",".",".",".",".",".",".",".","."]
    ,["5",".",".",".",".",".",".",".","."]
    ,["6",".",".",".",".",".",".",".","."]
    ,["7",".",".",".",".",".",".",".","."]
    ,["8",".",".",".",".",".",".",".","."]
    ,["9",".",".",".",".",".",".",".","."]]))

if __name__ == '__main__':
    main()