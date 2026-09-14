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
        Map<Node, Node> mymap = new HashMap<>();

        mymap.put(null, null);

        Node curr = head;
        while (curr != null) {
            mymap.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;
        while (curr != null) {
            mymap.get(curr).next = mymap.get(curr.next);
            mymap.get(curr).random = mymap.get(curr.random);
            curr = curr.next;
        }

        return mymap.get(head);
    }
}
