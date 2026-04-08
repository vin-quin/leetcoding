# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def solve(self, heights: list[int]) -> int:
        # Take l, r pointer and crunch in, storing max area along the way 

        # area = a*b
        realArea = 0

        theoryArea = {} # Most area possible this idx can have if it went from i to end
        for i in range(len(heights)):
            theoryArea[i] = heights[i] * (len(heights) - i)

        print(theoryArea)

        areas = list(theoryArea.items())
        areas.sort(key=lambda x: x[1], reverse=True)
        print(areas)

        for v in areas:
            idx, maxA = v
            print(idx, maxA)

            if maxA <= realArea: # We dont care to check anymore it cant get better
                print('donezo')
                break

            for i in range(idx, len(heights)):
                currArea = min(heights[idx], heights[i]) * (i-min(idx,1))
                print(f'{idx=}/{i=}/{currArea=}')
                if currArea > realArea:
                    realArea = currArea

        return realArea 


def main():
    s = Solution()
    print(s.solve([2,1,5,6,2,3]))
    # print(s.solve([2,4]))
    # print(s.solve([7,1,7,2,2,4]))
    # print(s.solve([1,3,7]))

if __name__ == '__main__':
    main()