# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def solve(self, height: list[int]) -> int:
        # Cannot trap with edge of graph (y-axis bar)


        # every n that is directly adjacent to a 0 is a possible fill point
        # keep moving left and right until left != 0 and right == 0, that's a fill point we start at

        # start left and increment until its nonzero then wait
        # right continues until it hits zero, saving the max height it finds
        # set l = maxHeight_i and continue incrementing right until it hits a nonzero heihgt again
        
        #   if right >= left, that is the max fill we can do so set it and then go back to searching for the next fill poit
        #   else continue incrementing right until we hit 0. Save max and use that to calculate fill between l & r.
        
        maxL, maxR= 0, 1
        l, r = 0, 1
        filled = 0
        fillable = False # Short circuit to track if it is even possible for the graph to be fillable
        while l < len(height)-1:
            filling = False

            if height[l] == 0:
                l += 1
                r += 1
                continue

            if height[l] >= height[maxL]:
                maxL = l

            if maxR == maxL: # Left met right so we need to swap over
                maxR += 1

            if height[r] < height[maxL]: # ! If we hit end of array while filling we cannot fill that area and result is 0 for that area
                filling = True

            # print(f'Checking: {l=}, {r=}, {maxL=}, {maxR=}')
            if filling:
                # go right until we exceed maxLeftHeight or hit a 0
                for i in range(r, len(height)):
                    if height[i-1] - height[i] < 0: # We increased because diff is negative
                        fillable = True

                    if height[i] >= height[maxL]: # We need to fill up to this point
                        maxR = i
                        break

                    if height[maxR] <= height[i]:
                        maxR = i

                if not fillable:
                    return filled
                # if gap between maxL and maxR <= 1 then we never found another end to fill, so we failed
                if maxR - maxL <= 1:
                    # print(f'Cannot fill between {maxL} and {maxR}')
                    l += 1
                    r += 1
                else: # succeeded
                    a = min(height[maxR], height[maxL])
                    b = maxR-maxL-1
                    c = sum(height[maxL+1:maxR])
                    fill = (a * b) - c
                    # print(f'Filling between {maxL} and {maxR} -> {fill}')
                    filled += fill
                    l = maxR
                    r = l + 1
                maxL = l
                maxR = r
            else:
                l += 1
                r += 1

        return filled
    
    def solveOptimal(self, height: list[int])-> int:
        # Greedy, we calc how much water can be stored at pos[i] given the heighest bar on the side
        # We build from the minimum of the two max bars found. This guarantees that if we haven't
        # found a max, we're always gonna get 0 since it spills out. If we have, then we logically know
        # we can fit SOMETHING SOMEWHERE inside so we build off of that assumption and work our way in.
        fill = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r] # wall values

        while l < r: 
            if maxL <= maxR:
                l += 1
                if maxL < height[l]:
                    maxL = height[l]
                fill += max(min(maxL, maxR) - height[l], 0)
            else:
                r -= 1
                if maxR < height[r]:
                    maxR = height[r]
                fill += max(min(maxL, maxR) - height[r], 0)

        return fill

def main():
    s = Solution()
    print(s.solveOptimal([0,7,1,4,6]))
    print(s.solveOptimal([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
    print(s.solveOptimal([5,4,1,2]))
    print(s.solveOptimal([4,2,3]))
    print(s.solveOptimal([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.solveOptimal([4,2,0,3,2,5]))
    print(s.solveOptimal([5,4,3,2,1]))

if __name__ == '__main__':
    main()