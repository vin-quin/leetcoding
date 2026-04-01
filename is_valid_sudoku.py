# https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def solve(self, board: list[list[str]]) -> bool:
        '''
        Each digit in a row can only appear once (1-9)
        Each digit in a column can only appear once (1-9)
        Each digit in 3x3 subgrid can only appear once (1-9)
        '''


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

if __name__ == '__main__':
    main()