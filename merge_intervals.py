# https://neetcode.io/problems/merge-intervals/question?list=blind75
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # We assume overlap is the range between i[0] and i[1], not only the given bounds
        if len(intervals) <= 0: 
            return []

        next, anchor = intervals[0], None
        groups = intervals.copy()
        i=0

        while  i < len(groups):
            anchor = groups[i]
            j = i+1
            recheck = False

            while j < len(groups): # Lookahead from anchor
                next = groups[j]

                upperBound, lowerBound = [], []

                if next[1] >= anchor[1]: # curr is the true upper bound
                    upperBound = next
                    lowerBound = anchor 
                else: # prev is the true upper bound
                    upperBound = anchor
                    lowerBound = next

                if lowerBound[1] >= upperBound[0]: # LB MAX within UB MIN then it must be in that range
                    print(f'Before: {groups=}')
                    print(f'Overlap: {lowerBound=}, {upperBound=}')
                    groups[i] = anchor = [min(lowerBound[0], upperBound[0]), upperBound[1]]
                    groups.pop(j)
                    print(f'After: {groups=}')
                    recheck = True
                else:
                    print(f'No overlap: {lowerBound=}, {upperBound=}')
                    # i += 1
                    j += 1

                print()
            if recheck:
                i = 0
            else: 
                i += 1

        return groups

def main():
    s = Solution()
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
    print()


if __name__ == '__main__':
    main()