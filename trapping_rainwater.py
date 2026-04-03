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
        
        maxR, maxL = 0, 0
        l, r = 0, 1
        filled = 0

        while l < len(height)-1:
            filling = False
            print(f'Checking: {l=}, {r=}')

            if height[l] == 0:
                l += 1
                r += 1
                continue

            if height[l] >= maxL:
                maxL = l

            if height[r] == height[maxL]: # ! If we hit end of array while filling we cannot fill that area and result is 0 for that area
                filling = True

            if filling:
                # go right until we exceed maxLeftHeight or hit a 0
                for i in range(r, len(height)):
                    if height[i] >= height[maxL]: # We need to fill up to this point
                        maxR = i
                        break

                    if height[maxR] < height[i]:
                        maxR = i

                # if maxR == 0 then we never found another end to fill, so we failed
                if maxR == 0:
                    print(f'Cannot fill between {maxL} and {maxR} -> {fill}')
                    return filled
                else: # succeeded
                    a = min(height[maxR], height[maxL])
                    b = maxR-maxL-1
                    c = sum(height[maxL+1:maxR])
                    fill = (a * b) - c
                    print(f'Filling between {maxL} and {maxR} -> {fill}')
                    filled += fill
                    l = maxR
                    r = l + 1
            else:
                l += 1
                r += 1

        return filled

def main():
    s = Solution()
    print(s.solve([0,1,0,2,1,0,1,3,2,1,2,1]))

if __name__ == '__main__':
    main()