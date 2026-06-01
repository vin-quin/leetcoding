# https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.insert(self.insert(0, len(self.nums)-1, val), val)
        return self.nums[self.k-1]

    def insert(self, l: int, r: int, v: int):
        if (l >= r):
            return l
        
        mid = l+(r-l)//2
        if (self.nums[mid] == v):
            return mid
        
        if (self.nums[mid] < v) :
            return self.insert(l, mid, v)
        else:
            return self.insert(mid+1, r, v)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)