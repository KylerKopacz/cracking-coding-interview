'''
Implement an algorithm to find the kth to last element of a singly linked list

ANALYSIS:
    - Runtime Complexity: O(n)
        - Worst case is
    - Space Complexity:
    - Best Case Runtime:
'''
import random
from LinkedList.LinkedList import LinkedList

def solver(ll, kth):
    # the ole runner technique, pretty slick eh?
    p1 = ll.head
    p2 = ll.head

    # move p2 out kth elements out
    for x in range(kth):
        p2 = p2.next
    
    # now move both at the same pace, and when p2.next is null, we can return the value at p1
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    
    # just like count dooku predicted
    return p1.value

def check_solutions(outputs, expected, inputs):
    # Check that they are the same size
    if len(outputs) != len(expected):
        print("Length Mismatch: size of outputs ({}) doesn't match expected ({})"
            .format(len(outputs, len(expected))))
        return
    
    # Run through all the solutions, and see what's up
    counter = 0
    for ans, exp, inp in zip(outputs, expected, inputs):
        if ans == exp:
            counter += 1
        else:
            print("======================================================")
            print("Wrong Answer: {} should equal {}".format(ans, exp))
            print("Input: {}".format(inp))
            print("======================================================\n")

    # print the final score
    print("FINAL SCORE: {}/{}".format(counter, len(inputs)))

if __name__ == "__main__":
    # create a random list of integers, so that we can create some random tests
    values = [random.randint(0,1000) for x in range(10000)]
    ll = LinkedList()
    for x in values:
        ll.addToTail(x)
    
    toGet = 0
    print("Value Returned from function: {}".format(solver(ll, toGet)))
    print("Correct Value: {}".format(values[len(values) - toGet - 1]))
