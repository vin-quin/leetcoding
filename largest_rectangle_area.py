# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def solve(self, heights: list[int]) -> int:
        # area = 0

        # anything involving index i can only be as big as the min height beside i except for i itself
        # r, l = 0, 0
        # [idx, allowedHeight]
        # while r < len(heights)
        #     area = min(height[r], height[l]) * max((r-l),1) # Fix 0,0 case
        #     if area > stack.peek
        #         stack.pop
        #         l += 1 # shrink window right
        #     else:
        #         r += 1 # expand window right

        #     s.push(i, min(height[r], height[l]))

        # [area, allowedheight]
        
        # R->L
        # 3
        # 2
        # 6
        # 5
        # 1
        # 2 

        # maxarea=0,3
        # while stack
        #     area = pop off top of stack
        #     area = max(area, min(maxArea[1], area) * (r-l)+1) # set area to 
        #     if area > maxarea
        #         maxarea = area, area.maxheight
        #     else 
        #         do nothing


        biggestArea = [heights[0], heights[0], 0] # [area, allowedHeight, startIdx]
        
        for i in range(1, len(heights)):
            bar = heights[i]
            currArea = min(bar, biggestArea[1]) * ((i-biggestArea[2])+1)
            print(f'Checking area: {bar=}, {currArea=}, {biggestArea=}')

            if  currArea > biggestArea[0]: # New biggesst area
                print('New biggest area')
                biggestArea = [currArea, min(bar, biggestArea[1]), i]
            # if minHeight(bararea, biggestarea) * (barI - biggestI)+1 > biggestArea
            #     biggestArea = barArea, minHeight
            
            if bar > biggestArea[0]: # The standalone bar is bigger than the combined area so far
                print('New biggest area from bar')
                biggestArea = [bar, bar, i]
            # if bararea > biggestarea
            #     biggest = bararea, bar

        print(f'{biggestArea=}')

        return biggestArea[0] 


def main():
    s = Solution()
    print(s.solve([2,1,5,6,2,3]))
    # print(s.solve([2,4]))
    # print(s.solve([7,1,7,2,2,4]))
    # print(s.solve([1,3,7]))

if __name__ == '__main__':
    main()