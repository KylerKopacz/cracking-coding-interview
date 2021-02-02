'''
Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
    - Well it would be really hard because you kinda have to have a memory of what you have seen already.
    - One idea is to just go number by number in the linked list and check for a certain number and iterate
    through the entire list everytime you come to a new number, and remove all the duplicates that you find of
    that value within the list.

ANALYSIS:
    - Runtime Complexity: O(n)
        - You have to touch all the nodes twice, one time for seeing that's in the list and the other
        one to remove all of the duplicates, which is done in one pass.
    - Space Complexity: O(n)
        - The worst case is that you have all unique values, and so you'll have to add all the values into the hash table. 
    - Best Case Runtime:
'''

from LinkedList.LinkedList import LinkedList

def solver(input):
    # use a hash table for efficient lookup
    seen = {}

    # run through the linked list, and append what we have seen before
    currNode = input.head
    while currNode.next != None:
        currNode = currNode.next
        if currNode.value not in seen:
            seen.append(currNode.value)

    # now we can go through and delete all the nodes that are duplicates
    p1 = input.head
    p2 = p1.next
    while(p2.next != None):
        # If the second node's value has been seen before, then we need to delete the node at p2
        if p2.value not in seen:
            p1.next = p2.next
            p2 = p2.next
            continue
        else:
            seen.remove(p2.value)
            p1 = p1.next
            p2 = p2.next

    # p2 should be at the end, but if the current value there has been seen, then we have to remove this node
    if p2.value not in seen:
        p1.next = None

    # return the new linked list
    return input

if __name__ == "__main__":
    # Create unsorted Linked list
    l1 = LinkedList()
    toAdd = [5,6,5,1,2,1,2]
    for x in toAdd:
        l1.addToTail(x)


    # do the problem
    print("========== RESULT ==========")
    solver(l1)
    l1.printList()

    # Create unsorted Linked list
    print("========== ANSWER ==========")
    s1 = LinkedList()
    ans = [5,6,1,2]
    for x in ans:
        s1.addToTail(x)
    s1.printList()
    
    
