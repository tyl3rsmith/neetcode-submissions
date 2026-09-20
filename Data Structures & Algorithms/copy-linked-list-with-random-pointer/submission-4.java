/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> oldToNew = new HashMap<>();

        Node curr = head;
        while (curr != null) {
            oldToNew.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;
        Node res = oldToNew.get(curr);
        Node dummy = new Node(0);
        dummy.next = res;
        
        while (curr != null) {
            res.next = oldToNew.get(curr.next);
            res.random = oldToNew.get(curr.random);

            res = res.next;
            curr = curr.next;
        }

        return dummy.next;
        
    }
}
