# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def solve(self, heights: list[int]) -> int:
        # Take l, r pointer and crunch in, storing max area along the way 

        # area = a*b
        maxArea = 0
        for i in range(len(heights)):
            l, r = i, i-1
            while r < len(heights):
                area = min(heights[l], heights[r]) * (r - l + 1) # Min gets us the max height to make a rect
                if area > maxArea:
                    print(l, r, area)
                    maxArea = area
                r += 1

        # O(N^2)
        return maxArea 


def main():
    s = Solution()
    print(s.solve([2,1,5,6,2,3]))
    print(s.solve([2,4]))

if __name__ == '__main__':
    main()