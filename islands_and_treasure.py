# https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150
from copy import deepcopy
class Solution:
    WATER = -1
    TREASURE = 0
    LAND = 2**31
    VISITED = -99
    CURR_CHEST_R = 0
    CURR_CHEST_C = 0

    def solve(self, grid: list[list[int]]) -> None:
        # Start with every chest location and flood fill out, first chest will flood entire board/connected land
        # Each subsequent chest floods until it cannot (the adj land has a diff closer chest than this one)
        chests = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == self.TREASURE:
                    chests.append([r,c])
        
        for pos in chests:
            visited = deepcopy(grid)
            self.CURR_CHEST_R = pos[0]
            self.CURR_CHEST_C = pos[1]

            self.flood(grid, visited, pos[0]+1, pos[1], 1)
            self.flood(grid, visited, pos[0]-1, pos[1], 1)
            self.flood(grid, visited, pos[0], pos[1]+1, 1)
            self.flood(grid, visited, pos[0], pos[1]-1, 1)
        
        for r in grid:
            print(r)

    def flood(self, grid: list[list[int]], visited: list[list[int]], r: int, c: int, dist: int):
        if not self.valid(grid, visited, r, c): # Nothing to do here
            return

        visited[r][c] = self.VISITED
        # Would this chest be closer than the currently closest chest to this position
        # dist = self.distance(r, c)

        if dist <= grid[r][c]:
            # Update and check all adjacent
            grid[r][c] = dist

            self.flood(grid, visited, r+1, c, dist+1)
            self.flood(grid, visited, r-1, c, dist+1)
            self.flood(grid, visited, r, c+1, dist+1)
            self.flood(grid, visited, r, c-1, dist+1)

    def valid(self, grid: list[list[int]], visited: list[list[int]], r: int, c: int) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and visited[r][c] != self.VISITED and grid[r][c] != self.WATER and grid[r][c] != self.TREASURE 

def main():
    s = Solution()
    print(s.solve([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]))

if __name__ == '__main__':
    main()