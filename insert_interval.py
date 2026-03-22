# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # If newInterval overlaps, it needs to merge with an existing interval(s)
        #   If it overlaps, multiple, merge them all
        # If newInterval does NOT overlap, just place where it should be in order

        # Binary search on newInterval_start to find nearest
        # Check result nad merge if necessary
        # Repeat for all remaining intervals til no more merge is possible
        idx = binary_search(intervals, newInterval[0])
        l = intervals[:idx]
        interval = [min(intervals[idx][0], newInterval[0]), max(intervals[idx][1], newInterval[1])]

        while intervals[idx][0] < newInterval[1]: # While we can merge intervals
            start, stop = intervals[idx][0], intervals[idx][1]

            if start <= interval[1]: # Merge
                interval[1] = max(stop, interval[1])

            idx += 1
            
        l += [interval]
        return l + intervals[idx:]


# Returns value closest to target (at or less) 
def binary_search(arr: list[list[int]], target: int):
    if len(arr) <= 0:
        return 0
    
    if len(arr) == 1:
        return 1 if target > arr[0][1] else 0
    
    mid = len(arr) // 2

    if arr[mid][0] == target:
        return mid
    elif arr[mid][0] <= target:
        return binary_search(arr[mid:], target)

    return binary_search(arr[:mid], target)

def main():
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

if __name__ == '__main__':
    main()