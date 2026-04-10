# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def solve(self, temperatures: list[int]) -> list[int]:
        temps = [0] * len(temperatures)
        stack = [] 
        # Always gonna end iin 0 since we have no further data
        # Waiting for THIS day to pass is inclusive so 73->74 = 1 day

        # let R=the first value greater than temperature at L
        # This means ANY value between L and R (excl) MUST be SMALLER than L
        # Else R would have appeared sooner 

        # If greater than L it absorbs the whole stack so problem solved
        # As a rule, for right side is always top of the stack, and the index being set to the result of R-L
        for i in range(len(temperatures)): 
            while stack and stack[-1][0] < temperatures[i]: # Today is hotter than top of stack 
                t = stack.pop()
                temps[t[1]] = i - t[1]

            stack.append([temperatures[i], i])

       
        return temps
    
    def solveBruteForce(self, temperatures: list[int]) -> list[int]:
        temps = []

        l, r = 0, 1
        while l < r < len(temperatures):
            if temperatures[l] < temperatures[r]:
                temps[l] = 1
            else: # Scan forward
                while r < len(temperatures):
                    if temperatures[l] < temperatures[r]:
                        temps[l] = r-l
                        break
                    r += 1
                else: # Never found a htter day
                    temps[l] = 0      

            l += 1
            r = l+1
       
        return temps


def main():
    s = Solution()
    # print(s.solve([73,74,75,71,69,72,76,73]))
    print(s.solve([30,40,50,60]))
    print(s.solve([30,60,90]))

if __name__ == '__main__':
    main()

'''
69,4
71,3
75,2
72,5 > stack.peek so pop off 69 and set it to 5-4 then continue

72,5
71,3
75,2
72 > stack.peek so pop off 71 and set it to 5-3 then continue

76,6
72,5
75,2
76 > stack.peek so pop off 72 and set it to 6-5 then continue
76 > stack.peek so pop off 75 and set it to 6-2 then continue

73,7
76,6
End of temps. Array already initialized ot 0 so we don't even need to clear the stack we are done
'''