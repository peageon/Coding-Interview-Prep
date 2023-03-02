#Looked at solution from neetcode and did it myself again
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #recommended solution was to find the middle divide into two and reverse the divdied half and merge

        first_half = head
        doubled = head.next
        while doubled and doubled.next:
            first_half = first_half.next
            doubled = doubled.next.next
        
        second_half = first_half.next
        first_half.next = None
        first_half = head
        #reverse second half
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        second_half = prev

        while first_half and second_half:
            temp = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp
            first_half = temp
            second_half = temp2

        