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
        // split the lists into two
        ListNode list1 = head;
        ListNode middle = findMiddle(head);
        ListNode list2 = middle.next;
        middle.next = null;

        list2 = reverseList(list2);
        mergeLists(list1, list2);
    }

    private void mergeLists(ListNode list1, ListNode list2) {
        while (list2 != null) {
            ListNode temp1 = list1.next;
            ListNode temp2 = list2.next;

            list2.next = list1.next;
            list1.next = list2;

            list1 = temp1;
            list2 = temp2;
        }

    }

    private ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }
}
