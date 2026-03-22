# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        start, stop = 0, len(height)-1
        area = 0

        while start != stop:
            cArea = min(height[start], height[stop]) * (stop-start)

            if cArea >= area:
                area = cArea

            if height[start] < height[stop]:
                start += 1
            else:
                stop -= 1

        return area
        

def main():
    s = Solution()
    print(s.maxArea([1,7,2,5,4,7,3,6]))
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,2,1]))

if __name__ == '__main__':
    main()