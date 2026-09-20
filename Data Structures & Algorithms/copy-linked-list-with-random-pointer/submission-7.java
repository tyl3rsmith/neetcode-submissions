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
        oldToNew.put(null, null);

        Node curr = head;
        while (curr != null) {
            if (!(oldToNew.containsKey(curr))) {
                oldToNew.put(curr, new Node(0));
            } 
            oldToNew.get(curr).val = curr.val;

            if (!(oldToNew.containsKey(curr.next))) {
                oldToNew.put(curr.next, new Node(0));
            }
            oldToNew.get(curr).next = oldToNew.get(curr.next);

            if (!(oldToNew.containsKey(curr.random))) {
                oldToNew.put(curr.random, new Node(0));
            }
            oldToNew.get(curr).random = oldToNew.get(curr.random);
            curr = curr.next;
        } 

        return oldToNew.get(head);
    }
}
