# https://leetcode.com/problems/reorder-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        while slow:
            prev = slow
            fast = slow.next
            while fast and fast.next: # Find tail
                prev = fast
                fast = fast.next
                if fast.next == slow: # Only can happen on cycle
                    fast.next = None

            prev.next = None
            fast.next = slow.next
            slow.next = fast

            slow = fast.next # We don't want to reorder the one we just swapped

        return head
    
def main():
    s = Solution()
    print(s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

if __name__ == '__main__':
    main()