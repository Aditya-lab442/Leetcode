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
    public void reorderList(ListNode head) {
        ListNode temp = head;
        ArrayList<Integer> a = new ArrayList<>();
        while(temp!=null){
            a.add(temp.val);
            temp = temp.next;
        }
        int flag = 0;
        int left = 0;
        int right = a.size()-1;
        temp = head;
        while(left<=right){
            if(flag==0){
                temp.val = a.get(left);
                left++;
                flag=1;
            }
            else{
                temp.val = a.get(right);
                right--;
                flag=0;
            }
            temp = temp.next;
        }
    }
}