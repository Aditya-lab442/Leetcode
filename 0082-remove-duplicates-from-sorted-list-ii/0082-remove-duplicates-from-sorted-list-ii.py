# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        ans = None
        curr = None
        for element in temp:
            if temp.count(element) == 1:
                new_node = ListNode(element)

                if ans is None:
                    ans = new_node
                    curr = new_node
                else:
                    curr.next = new_node
                    curr = new_node
        return ans
