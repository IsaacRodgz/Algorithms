// HackerRank

/*
  Find merge point of two linked lists
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/

/*
[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q
*/

// @param headA : Head node of linked list A
// @param headB : Head node of linked list B
// @return Node. Node value where both lists get merged

int FindMergeNode(Node headA, Node headB) {
    Deque<Node> stackA = new ArrayDeque<>();
    Deque<Node> stackB = new ArrayDeque<>();
    
    while(headA != null){
        stackA.push(headA);
        headA = headA.next;
    }
    while(headB != null){
        stackB.push(headB);
        headB = headB.next;
    }
    int last = 0;
    while(stackA.peekFirst() == stackB.peekFirst()){
        last = stackA.pop().data;
        stackB.pop();
    }
    return last;
}
