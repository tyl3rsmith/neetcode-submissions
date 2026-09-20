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
            // check to see if this current node has been cloned
            if (!oldToNew.containsKey(curr)) {
                oldToNew.put(curr, new Node(curr.val));
            }
            Node copy = oldToNew.get(curr);

            // check to see if the next node has been cloned
            if (!oldToNew.containsKey(curr.next)) {
                oldToNew.put(curr.next, new Node(curr.next.val));
            }
            copy.next = oldToNew.get(curr.next);

            // check to see if the random node has been cloned
            if (!oldToNew.containsKey(curr.random)) {
                oldToNew.put(curr.random, new Node(curr.random.val));
            }
            copy.random = oldToNew.get(curr.random);

            curr = curr.next;
        }

        return oldToNew.get(head);
    }
}
