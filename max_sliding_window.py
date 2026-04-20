# https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        q = [(i, nums[i]) for i in range(k)]
        maxN = max(q, key=lambda x: x[1])
        # print(q)
        # print(maxN)

        # MaxStack
        # Add nums[i] to stack
        # while stack.getMax is OOB
        #     stack.popMax

        # q.append(i, nums[stack.getMax])

        maxWindow = [maxN]

        # i is left ptr, i+k is. right
        for i in range(k, len(nums)):
            rem = q.pop(0) # Front element has been replaced
            q.append((i, nums[i]))
            # print(q)

            if rem[1] == maxN[1]: # No longer in bounds we need to search for anew max or we just removed our max
                maxN = max(q, key=lambda x: x[1])
            else:
                if maxN[1] <= q[-1][1]: # Replace with our new max or the same later max
                    maxN = q[-1]
                
            maxWindow.append(maxN)

        return [t[1] for t in maxWindow]


def main():
    s = Solution()
    print(s.solve([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
    print(s.solve([1], 1), [1])
    print(s.solve([-7, -8, -7, 5, 7, 1, 6, 0], 4), [5, 7, 7, 7, 7])

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