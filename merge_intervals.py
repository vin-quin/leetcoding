# https://neetcode.io/problems/merge-intervals/question?list=blind75
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # We assume overlap is the range between i[0] and i[1], not only the given bounds
        if len(intervals) <= 0: 
            return []

        curr, prev = intervals[0], None
        groups = intervals.copy()
        i=1

        while  0 < i < len(groups):
            prev = groups[i-1]
            curr = groups[i]

            upperBound, lowerBound = [], []

            if curr[1] >= prev[1]: # curr is the true upper bound
                upperBound = curr
                lowerBound = prev 
            else: # prev is the true upper bound
                upperBound = prev
                lowerBound = curr

            if lowerBound[1] >= upperBound[0]: # LB MAX within UB MIN then it must be in that range
                print(f'Before: {groups=}')
                print(f'Overlap: {lowerBound=}, {upperBound=}')
                groups.pop(i-1)
                groups[i-1] = [min(lowerBound[0], upperBound[0]), upperBound[1]]
                print(f'After: {groups=}')
                i = 1
            else:
                print(f'No overlap: {lowerBound=}, {upperBound=}')
                i += 1

            print()

        return groups

def main():
    s = Solution()
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
    print()
    print(s.merge([[1,4],[0,2],[3,5]]))
    print()


if __name__ == '__main__':
    main()