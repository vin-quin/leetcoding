# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def solve(self, heights: list[int]) -> int:
        # anything involving index i can only be as big as the min height beside i except for i itself
        heights.append(0) # We add a known good endpoint. This wont impact area calcs 
        stack = [0]
        area = heights[0]

        # Conceptually, we are going through each bar in order and pushing them to the stack as long as they are
        # strictly increasing in order. Once that condition is false, we begin unwinding the stack using the 
        # breaking condition as our right boundary. Each item popped from the stack uses the NEXT item in the stack
        # as a left boundary to calc the area in the range. The left boundary is EXCLUSIVE as we use the popped
        # index to get the best possible area. Naturally this means we will eventually hit a value in the stack with NO
        # left boundary, but we must still reduce it to the next "lesser" boundary that is not itself. 
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]: # Curr is smaller than top of stack, right boundary found
                # print(f'Top of stack > heights[i]: {heights[stack[-1]]} > {heights[i]} -> {area=}')
                # Pop stack until the current is LARGER than stack top again or empty, whwatever comes first
                idx = stack.pop()
                
                # Because we do NOT want to include our left boundary, which is at the bototm of the stack, 
                # We check for this specific case
                if stack:
                    left = stack[-1]
                else: 
                    left = -1

                # We calc area as we go, since we know the stack is increasing taking the idx's height is guaranteed
                # To be the best height we can do
                currArea = heights[idx] * (i - left - 1)
                if currArea > area:
                    area = currArea

            stack.append(i)
        
        return area


def main():
    s = Solution()
    print(s.solve([2,1,5,6,2,3]), 10)
    print(s.solve([2,4]), 4)
    print(s.solve([7,1,7,2,2,4]), 8)
    print(s.solve([1,3,7]), 7)
    print(s.solve([9,0]), 9)
    print(s.solve([0,9]), 9)
    print(s.solve([0]), 0)
    print(s.solve([1,8,9]), 16)
    print(s.solve([4,2,0,3,2,4,3,4]), 10)
    print(s.solve([0,3,2,4,3,4]), 10)

if __name__ == '__main__':
    main()