# https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def solve(self, board: list[list[str]]) -> bool:
        '''
        Each digit in a row can only appear once (1-9)
        Each digit in a column can only appear once (1-9)
        Each digit in 3x3 subgrid can only appear once (1-9)
        '''
        freqs = {str(i+1): 0 for i in range(9)}
        for i in range(len(board)):
            seenRow = set()
            seenCol = set()
            for j in range(len(board[i])):             
                if board[i][j] != '.':
                    if board[i][j] in seenRow: # Duplicate num in row
                        return False
                    seenRow.add(board[i][j])
                    freqs[board[i][j]] += 1

                if board[j][i] != '.':
                    if board[j][i] in seenCol: # Duplcate num in col
                        return False
                    seenCol.add(board[j][i])
                    freqs[board[j][i]] += 1
                
        # SUBGRID_N=3
        # rOffset, cOffset = 0, 0
        # for i in range(SUBGRID_N):
        #     for row in range(rOffset, SUBGRID_N+rOffset): 
        #         for col in range(cOffset, SUBGRID_N+cOffset):
        for v in freqs.values(): # Pretty sure any non-even frequencies mean the board is invalid
            if v % 2 != 0:
                return False
                
        return True


def main():
    s = Solution()
    print(s.solve([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    
    print(s.solve([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

if __name__ == '__main__':
    main()