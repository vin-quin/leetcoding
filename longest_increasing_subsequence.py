# https://leetcode.com/problems/longest-increasing-subsequence/description/ 
class Solution:
    def solve(self, nums: list[int]) -> int:
        longest = []
        l, r = 0, 1

        if len(nums) <= 1:
            return len(nums)
        
        for l in range(len(nums)):
            sequence = [nums[l]]

            for r in range(l+1, len(nums)):
                # while nums[r] > nums[r-1]:
                print(f'{r=}/{nums[r]=}/{nums[r-1]=}')
                if nums[r] < nums[r-1]:
                    print('Not increasing - break')
                    break # no longer increasing
                sequence.append(nums[r])
            
            if len(sequence) > len(longest):
                longest = sequence
                print(f'New longest: {longest}')
        

            print(f'{sequence=}')
        print(f'{longest=}')

        return len(longest)


def main():
    s = Solution()
    print(s.solve([10,9,2,5,3,7,101,18]))

if __name__ == '__main__':
    main()