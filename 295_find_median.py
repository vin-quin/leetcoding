# https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:
    median = None
    nums = []

    def __init__(self):
        ...

    def addNum(self, num: int) -> None:
        if len(self.nums) == 0:
            self.median = num

        heapq.heappush(self.nums, num)

    def findMedian(self) -> float:
        nums = heapq.nlargest((len(self.nums)//2)+1, self.nums) # Go one further back and we combine those last two digits for median
        if len(self.nums) % 2 != 0: # if len(self.nums) % 2 != 0: # sorted so the smallest at the halfway should be median for odds
            return nums[-1]
        
        return (nums[-1]+nums[-2])/ 2
        

# Store the first median as an up to PQ
# Any new number greater than median goes into a new overMedian PQ
# If the sum of size of both pqs is even we calc with highest from lower median and lowest from higherMedianFinder medianFinder = new MedianFinder()
medianFinder = MedianFinder()
print(medianFinder.addNum(1))    # arr = [1]
print(medianFinder.findMedian()) # return 1.0
print(medianFinder.addNum(3))    # arr = [1, 3]
print(medianFinder.findMedian()) # return 2.0
print(medianFinder.addNum(2))    # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0