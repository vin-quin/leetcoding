# https://leetcode.com/problems/3sum/description/
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        '''
        i != j
        i != k
        j != k

        each index is unique and sums to 0
        '''
        locs = {}
        for i in range(len(nums)):
            locs[nums[i]] = i

        triples = []

        nums.sort()
        
        for i in range(len(nums)//2): # Feel like we only need to check half 
            l, r = i+1, len(nums)-1

            while r > l:
                if nums[i] + nums[l] + nums[r] == 0 and (i != r and i != l):    
                    triples.append([nums[i], nums[l], nums[r]])
                    break
                r -= 1           

        print(triples)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = nums[i] + nums[j]
                n = s

                if s > 0: # need neg
                    n = -abs(s)
                else: # need pos 
                    n = abs(s)

                if n in locs and (i != j and i != locs[n] and j != locs[n]):
                    triples.append([nums[i], nums[j], n])

        res = list(map(lambda v: sorted(v), triples))
        v = []
        for i in res:
            if i not in v:
                v.append(i)

        return v


def main():
    s = Solution()
    print(s.solve([-1,0,1,2,-1,-4]))
    print(s.solve([0,1,1]))
    print(s.solve([0,0,0]))

if __name__ == '__main__':
    main()