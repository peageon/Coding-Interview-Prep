#reverse linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head

        while cur_node:
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp
        return prev_node