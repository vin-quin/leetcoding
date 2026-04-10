# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def solve(self, temperatures: list[int]) -> list[int]:
        temps = [0] * len(temperatures)
        stack = [0] # Preload with 0 since our last day will always be 0
        # Always gonna end iin 0 since we have no further data
        # Waiting for THIS day to pass is inclusive so 73->74 = 1 day

        # [1,1,1,0,0,0,0]
        # [73,74,75,71,69,72,76,73]
        # [1,1,1+1+1+1,1+1,1,1,0,0]

        # for i in range(len(temperatures)-2, -1 , -1):
        #     if temperatures[i] < temperatures[i+1]:
        #         temps[i] = 1
        #     else:
        #         temps[i] += temps[i+1]
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
    print(s.solve([73,74,75,71,69,72,76,73]))

if __name__ == '__main__':
    main()