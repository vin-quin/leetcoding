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

        charKey = {}

        for y in range(len(board)):
            for x in range(len(board[0])):
                c = board[y][x]
                if c in charKey:
                    charKey[c].append((x, y))
                else: 
                    charKey[c] = [(x, y)]

        # print(charKey)

        found = []
        for w in words:
            if w[0] not in charKey: # First letter isn't on board it can't exist
                continue

            locs = charKey[w[0]]
            # print(f'Checking locs for {w[0]=}')
            used = set()
            for coord in locs:
                used.add(f"{coord[0]}{coord[1]}")
                # print(f'Checking {coord=}')
                r = checkNeighbors(board, w[1:], coord[0], coord[1], used)
                if r:
                    found.append(w)
                    # print(f'Found: {found}')
                    break # Done

        return found

def isTarget(board: list[list[str]], x: int, y: int, target: str, used):
    if 0 <= y < len(board) and 0 <= x < len(board[0]) and f"{x}{y}" not in used:
        return target == board[y][x]
    
    return False

def checkNeighbors(board, word, x, y, used):
    # print(f'Checking for {word}')
    if word == "": # We found the word on the board
        # print("SUCCESS")
        return True 
    
    target = word[0]
    # print(f'{target=}')
    # print(f'{used=}')

    # print(f'{isTarget(board, x, y+1, target, used)=}')
    if isTarget(board, x, y+1, target,used):
        used.add(f"{x}{y+1}")
        if checkNeighbors(board, word[1:], x, y+1, used):
            return True
    # print(f'{isTarget(board, x, y-1, target,used)=}')
    if isTarget(board, x, y-1, target,used):
        used.add(f"{x}{y-1}")
        if checkNeighbors(board, word[1:], x, y-1, used):
            return True
    # print(f'{isTarget(board, x+1, y, target,used)=}')
    if isTarget(board, x+1, y, target,used):
        used.add(f"{x+1}{y}")
        if checkNeighbors(board, word[1:], x+1, y, used):
            return True
    # print(f"{isTarget(board, x-1, y, target,used)=}")
    if isTarget(board, x-1, y, target,used):
        used.add(f"{x-1}{y}")
        if checkNeighbors(board, word[1:], x-1, y, used):
            return True
    
    # print("FAIL")
    return False # We cannot continue building the word from this position

'''
[
 ["a","b","c"],
 ["a","e","d"],
 ["a","f","g"]
]


'''

def main():
    s = Solution()
    # print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
    # print(s.findWords([["a","b"],["c","d"]], ["aba"]))
    print(s.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], ["eaabcdgfa"]))

if __name__ == '__main__':
    main()