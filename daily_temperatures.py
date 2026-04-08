# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def solve(self, temperatures: list[int]) -> list[int]:
        temps = [] * len(temperatures)
        stack = [0] # Preload with 0 since our last day will always be 0
        # Always gonna end iin 0 since we have no further data
        # Waiting for THIS day to pass is inclusive so 73->74 = 1 day

        for t in temperatures:

        
        dp = [1,1,2,0,2,1,0,0]

        [73,74,75,71,69,72,76,73]


        6
        3
        2

        [1,1,4,3,1,1,0,0]

        [69,71,72,73,73,74,75,76]

        [69,]
        [72,1] # Not new max in stack so count+1
        [76,0] # New max in stack = 0 distance
        [73,0] # New max in stack = 0 distance

        if t[i] < t[i+1]:
            dp[i] = 1
        else:
            dp[i] = dp[i+1] + 1


        if i < i+1:
            go next
        else:
            keep going until i < i+1 or end of array
            repeat for next i in array

        76
        ---
        72
        69
        71
        75


        return temps


def main():
    s = Solution()
    print(s.solve([73,74,75,71,69,72,76,73]))

if __name__ == '__main__':
    main()