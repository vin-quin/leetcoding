# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def solve(self, temperatures: list[int]) -> list[int]:
        temps = [] * len(temperatures)

        # Always gonna end iin 0 since we have no further data
        # Waiting for THIS day to pass is inclusive so 73->74 = 1 day

        

        return temps


def main():
    s = Solution()
    print(s.solve([73,74,75,71,69,72,76,73]))

if __name__ == '__main__':
    main()