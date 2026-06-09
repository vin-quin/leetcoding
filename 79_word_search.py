# https://leetcode.com/problems/word-search/description/
from copy import deepcopy


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        b = deepcopy(board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.checkNeighbor(b, [row,col], word, 0):
                    return True

        return False

    def checkNeighbor(
        self, board: list[list[str]], pos: list[int], word: str, idx: int
    ) -> bool:
        r, c = pos[0], pos[1]

        if idx >= len(word):  # Reached end of word successuflly
            return True

        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != word[idx]:
            return False

        board[r][c] = '0'

        return (
            self.checkNeighbor(board, [r, c + 1], word, idx + 1)
            or self.checkNeighbor(board, [r, c - 1], word, idx + 1)
            or self.checkNeighbor(board, [r - 1, c], word, idx + 1)
            or self.checkNeighbor(board, [r + 1, c], word, idx + 1)
        )


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
