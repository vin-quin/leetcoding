# https://leetcode.com/problems/3sum/description/
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        '''
        i != j
        i != k
        j != k

        each index is unique and sums to 0
        '''
        # [-4,-1,-1,0,1,2]
        #      i    l r  
        # for i in range(len(nums)):
        #     while l < r and i != l != r:
        #         i + l + r == 0:
        #             correct
        #         i + l + r < 0: 
        #             left += 1
        #         else
        #             r -= 1

        # return v

        nums.sort()
        triplets = []
        # Sliding window from i to end of arr crunching in ot find a valid triple if exists
        for i in range(len(nums)-2): # We are scanning in 3's so don't need to check last 2
            l, r = i+1, len(nums)-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0 and i != l and l != r:
                    triple = sorted([nums[i], nums[l], nums[r]])
                    triplets.append(triple) if triple not in triplets else ...
                    # break # We cannot have another triplet from nums[i] that satisfies reqs, go next
                    l += 1
                elif s <= 0:
                    l += 1
                else:
                    r -= 1

        return triplets


def main():
    s = Solution()
    print(s.solve([-1,0,1,2,-1,-4]))
    print(s.solve([0,1,1]))
    print(s.solve([0,0,0]))
    print(s.solve([0,0,0,0]))
    print(s.solve([-2,0,1,1,2]))

if __name__ == '__main__':
    main()