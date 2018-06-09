// HackerRank

/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as  
  class Node {
     int data;
     Node next;
  }
*/

// Solution with pointers to nodes
Node Reverse(Node head) {

    if(head == null)
        return null;
    else if(head.next == null)
        return head;
    
    Node current = new Node();
    Node next = new Node();
    
    current = head.next;
    head.next = null;
    
    while(current.next != null){
        next = current.next;
        current.next = head;
        head = current;
        current = next;
        next = current.next;
    }
    current.next = head;
    head = current;
    
    return head;
}

// Solution with stack Data Structure
Node Reverse(Node head) {

    Stack<Node> node_stack = new Stack<Node>();
    while(head.next != null){
        node_stack.push(head);
        head = head.next;
    }
    Node first = head;
    while(!node_stack.isEmpty()){
        head.next = node_stack.pop();
        head = head.next;
    }
    head.next = null;
    return first;
}

// Recursive solution
Node Reverse(Node head) {

    if(head == null || head.next == null)
        return head;
    
    Node remaining = Reverse(head.next);
    head.next.next = head;
    head.next = null;
    
    return remaining;
}
