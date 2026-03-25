# https://leetcode.com/problems/word-search-ii/description/
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        '''
        board is 12x12 at MOST (144 chars)
        Letters/cells are consumed when used for a given word
        Words can be backwards (eat -> tae)
        Max 10 chars per given word
        Max 30000 words to check
        
        Prepass on the board and store each letter and its starting coordinates for quick checks:
        {
         'a': [[0,0], [1,0]...]
         ...
        }
        O(N)

        for each word, find the first letter on the grid and recursively search neighbors 
        with a "fan out" method. Either the next letter in the word will be in neighbors and we
        continue until the word is found. Else we check the next starting position of that letter
        until all are exhausted and we know the word cannot exist.

        O(W + 4(M))
        '''


def main():
    s = Solution()
    print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))

if __name__ == '__main__':
    main()