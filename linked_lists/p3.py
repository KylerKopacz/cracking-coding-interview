'''
NOTE: This question is actually horrible. Very poor wording and doesn't make sense. You are literally
accessing the data of the next node. Really big stinky bad!

Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE
    input:the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a ->b->d->e->f

ANALYSIS:
    - Runtime Complexity: O(1)
        - The only node that we are touching is the current node and apparently the next node,
        even though the question says that we don't have access to any of the other nodes.
    - Space Complexity: O(1)
        - We have constant space. This is pretty much a script to be honest.
    - Best Case Runtime: O(1)
        - we made it as fast as possible and that's pretty lit.
'''
from LinkedList.LinkedList import LinkedList

def solver(input):
    if input == None:
        return False
    
    # just swap the value of the current node with the value of the next node
    next = input.next
    input.value = next.value
    input.next = next.next

    return True

if __name__ == "__main__":
    values = [1,2,3,4,5,6,7,8,9]
    ll = LinkedList()
    ll2 = LinkedList()
    for x in values:
        ll.addToTail(x)
        if x != 5:
            ll2.addToTail(x)

    curr = ll.head
    while curr.value != 5:
        curr = curr.next
    
    # now that we have 5, pass that value into the function
    solver(curr)

    ll.printList()
    ll2.printList()

