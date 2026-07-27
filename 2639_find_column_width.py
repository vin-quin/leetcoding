# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        nums = []
        row, col = 0, 0

        for col in range(len(grid[0])):
            width = len(str(grid[row][col]))

            for row in range(len(grid)):
                width = max(width, len(str(grid[row][col])))
            
            nums.append(width)

        return nums


'''
[
[2911,-805,5477,-3349,163,-6644],
[4851,2990,2578,1124,2897,-1781],
[-2153,1774,-8238,-2894,4845,9608]
]
'''

def main():
    s = Solution()
    # print(s.findColumnWidth([[1],[22],[333]]))
    # print(s.findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))
    print(s.findColumnWidth([[2911,-805,5477,-3349,163,-6644],[4851,2990,2578,1124,2897,-1781],[-2153,1774,-8238,-2894,4845,9608]]))

if __name__ == '__main__':
    main()