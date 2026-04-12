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


        # biggestArea = [heights[0], heights[0], 0] # [area, allowedHeight, startIdx]
        # Stack of all bars
        # Each bar is a boundary, pop 2 first is right second is left
        # We will work backwards from the array. If the left boundary si smaller, replace it with next on stack
        # If right is smaller, replace it with left boundary then pull new left from stack
        stack = [[b, i] for i, b in enumerate(heights)] # [height, idx]
        r = stack.pop() # Always have 1 element to pull
        area = r[0]
        # print(f'Starting area: {area}')

        while stack:
            l = stack.pop()
            currArea = min(r[0], l[0]) * ((r[1]-l[1])+1)
            # print(f'{l=}/{r=} - Current area: {min(r[0], l[0])} * {(r[1]-l[1])+1} = {currArea}')
            if currArea > area:
                # print(f'New area PB: {currArea} - Old: {area}')
                area = currArea

            if r[0] < l[0]:
                r = l
            else:
                r[0] = min(r[0], l[0])

        return area


def main():
    s = Solution()
    print(s.solve([2,1,5,6,2,3]))
    print(s.solve([2,4]))
    print(s.solve([7,1,7,2,2,4]))
    print(s.solve([1,3,7]))

if __name__ == '__main__':
    main()