# https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        q = []
        maxQ = [] # high...low

        for i in range(k):
            q.append(nums[i])

            while maxQ and nums[maxQ[-1]] < nums[i]: # Remove smaller vals 
                maxQ.pop()
            maxQ.append(i)

        maxWindow = [nums[maxQ[0]]]

        # We simply maintain two queues, the first is the current window (q)
        # The second is a monotonically decreasing q (maxQ) keeping the index
        # So the index of the max is left, second max is idx 1, etc...
        # Each new max replaces every smaller val in the maxQ since a new max always comes after
        # So its always in the new range. 
        for i in range(k, len(nums)):
            q.pop(0) # Front element has been replaced
            q.append(nums[i])

            # Check if curr max is inbounds still
            while maxQ and maxQ[0] <= i-k: # maxQ idx < i-k = OOB
                maxQ.pop(0)

            # Check for a new max, replace every smaller val with this. It dominates them
            while maxQ and nums[maxQ[-1]] < nums[i]:
                maxQ.pop()
        
            maxQ.append(i) 
            maxWindow.append(nums[maxQ[0]])

        return maxWindow


def main():
    s = Solution()
    print(s.solve([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
    print(s.solve([1], 1), [1])
    print(s.solve([-7, -8, -7, 5, 7, 1, 6, 0], 4), [5, 7, 7, 7, 7])
    print(s.solve([1,-1], 1), [1,-1])

if __name__ == '__main__':
    main()
'''
// Take the max of EACH window and add that. Same logic applies the first
// Window is our starting max and it only changes by 1 each time so
// A single check tells us the new max in the current window
// O(N)

// Monotonically increasing stack of size k
// Store as pairs of (index,value)
// If index is OOB pop it its dead forever
// Else if new N is a new max we can clear the stack
//  Because we're guaranteed this new max at minimum for the next K elements

// Store the index of the max in THIS window
// If new int is BIGGER than max
    // We update the new max it and continue no scan needed
// If index is out of bounds 
    // We need to scan this window again fora new max


// The first window is the initial max window
int[] maxWindow = new int[nums.length];
int maxN = nums[0]; // Biggest num in max window. This must be exceeded to take a new max

// We check the initial k elements to get the starting max
for (int i = 1; i < k; i++) {
    if (nums[i] > maxN) {
        maxN = nums[i];
    }
}

// Check each next in window til we are done

return maxWindow;'''