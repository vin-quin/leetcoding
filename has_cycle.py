# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def solve(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False 
        seen = set()
        seen.add(head)

        curr = head.next
        while curr:
            if curr in seen:
                return True 
            
            seen.add(curr)
            curr = curr.next
    
        return False


def main():
    s = Solution()
    print(s.solve())

if __name__ == '__main__':
    main()