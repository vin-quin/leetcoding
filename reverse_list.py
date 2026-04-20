# https://leetcode.com/problems/reverse-linked-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ...


def main():
    s = Solution()
    print(s.solve(ListNode(1, ListNode(2))))

if __name__ == '__main__':
    main()