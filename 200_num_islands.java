/**
 * https://leetcode.com/problems/number-of-islands/description/
 */

class Solution {
    public int solve(char[][] grid) {
        int islands = 0;

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '1') {
                    islands++;
                    flood(grid, row, col);
                }
            }
        }

        return islands;
    }

    // Flood an island to get it off the map
    public void flood(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length) {
            return;
        }

        if (col < 0 || col >= grid[0].length) {
            return;
        }

        if (grid[row][col] != '1') {
            return;
        }

        grid[row][col] = '0';
        flood(grid, row+1, col);
        flood(grid, row-1, col);
        flood(grid, row, col-1);
        flood(grid, row, col+1);
    }
}
