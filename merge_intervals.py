# https://neetcode.io/problems/merge-intervals/question?list=blind75
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # We assume overlap is the range between i[0] and i[1], not only the given bounds
        # [1, 7] and [3, 5]
        # We know i[0] <= i[1]

        if len(intervals) <= 0: 
            return []

        curr, prev = intervals[0], None
        groups = intervals.copy()
        i=1

        while i < len(groups):
            prev = curr
            curr = groups[i]

            upperBound, lowerBound = [], []

            if curr[1] >= prev[1]: # curr is the true upper bound
                upperBound = curr # [5,20]
                lowerBound = prev # [15,16]
            else: # prev is the true upper bound
                upperBound = prev
                lowerBound = curr

            if lowerBound[1] >= upperBound[0]: # LB MAX within UB MIN then it must be in that range
                print(f'Before: {groups=}')
                print(f'Overlap: {lowerBound=}, {upperBound=}')
                groups.pop(i-1)
                groups[i-1] = [min(lowerBound[0], upperBound[0]), upperBound[1]]
                print(f'After: {groups=}')
            else:
                print(f'No overlap: {lowerBound=}, {upperBound=}')
                i += 1

            print()
            # Assumes i1 >= i0
            # if i0[0] >= i1[0] and UB check then it is in range
            # if i0[1] <= i1[1] then it is in range
            # [2,3] and [1,5]
            # [1,20] and [15, 16] sort by range size, higher range = i1

            # This works partially, if any number in either interval overlaps then it is valid,
            # Current check requires that all of i1 exist within i0 which is too strict
            # i1=[1,20] and i0=[15,25] 

        return groups

def main():
    s = Solution()
    print(s.merge([[1,3],[1,5],[6,7]]))
    print()
    print(s.merge([[15,20],[16,17], [13, 21], [1,3]]))
    print()
    print(s.merge([[1,2], [2,3]]))
    print()

if __name__ == '__main__':
    main()