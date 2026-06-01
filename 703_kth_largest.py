# https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        if (len(self.nums) == 1):
            self.nums.insert(0, val) if self.nums[0] < val else self.nums.append(val)
        else:
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
# obj = KthLargest(1, [-2])
# param_1 = obj.add(-3)
# print(param_1)
obj = KthLargest(3, [4,5,8,2])
param_1 = obj.add(3)
print(param_1)