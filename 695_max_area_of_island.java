/**
 * https://leetcode.com/problems/max-area-of-island/description/
 */
class Solution {
    public int solve(int[][] grid) {
        int area = 0;

        for (int r =0; r < grid.length; r++) {
            for (int c=0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    area = Math.max(area, flood(grid, r, c));
                }
            }
        }

        return area;
    }

    public int flood(int[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] != 1) {
            return 0;
        }

        grid[row][col] = -1; // Remove so we dont recount
        return 1+flood(grid, row-1,col)+flood(grid,row+1,col)+flood(grid,row,col-1)+flood(grid,row,col+1);
    }
}
