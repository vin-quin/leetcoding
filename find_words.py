# https://leetcode.com/problems/word-search-ii/description/
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        '''
        board is 12x12 at MOST (144 chars)
        Letters/cells are consumed when used for a given word
        Words can be backwards (eat -> tae)
        
        '''

def main():
    s = Solution()
    print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))

if __name__ == '__main__':
    main()