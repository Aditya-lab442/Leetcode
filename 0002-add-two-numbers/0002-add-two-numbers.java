/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = null;
        ListNode temp = null;
        int carry = 0;
        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;
            if (ans == null) {
                ListNode temp1 = new ListNode(sum % 10, null);
                ans = temp = temp1;
                carry = sum / 10;
                l1 = l1.next;
                l2 = l2.next;
                continue;
            }
            ListNode temp1 = new ListNode(sum % 10, null);
            ans.next = temp1;
            ans = temp1;
            carry = sum / 10;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l2 == null) {
            while (l1 != null) {
                int sum = l1.val + carry;
                ListNode temp1 = new ListNode(sum % 10, null);
                ans.next = temp1;
                ans = temp1;
                carry = sum / 10;
                l1 = l1.next;
            }
            if (carry > 0) {
                ListNode temp1 = new ListNode(carry % 10, null);
                ans.next = temp1;
            }
        } else if (l1 == null) {
            while (l2 != null) {
                int sum = l2.val + carry;
                ListNode temp1 = new ListNode(sum % 10, null);
                ans.next = temp1;
                ans = temp1;
                carry = sum / 10;
                l2 = l2.next;
            }
            if (carry > 0) {
                ListNode temp1 = new ListNode(carry % 10, null);
                ans.next = temp1;
            }
        }
        return temp;
    }
}