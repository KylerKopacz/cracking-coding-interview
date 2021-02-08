'''
Given a sorted (increasing order) array with unique integer elements, write an algo­
rithm to create a binary search tree with minimal height.
'''
from random import randint
from enum import Enum

# States to make visited states easier to work with
class NodeState(Enum):
    UNVISITED = 0
    VISITED = 1

# create a node class that we can use for these problems
class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None, None]
        self.state = NodeState.UNVISITED

    def setChild(self, node, childIdx):
        # if childIdx = 0, then it's the left child
        # if childIdx = 1, then it's the right child
        if childIdx == 0:
            self.children[0] = node
        else:
            self.children[1] = node

def assembleTree(tree):
    # The idea is to just keep splitting the array in half, and the root for each subtree is going to be that half

    # make sure that we can at least access index 0, otherwise we cannot create current node to return
    if len(tree) == 0:
        return

    # we want to get the root node
    rootIdx = len(tree) // 2

    # If the root index is 0, then we have reached the bottom of the tree
    if rootIdx == 0:
        return Node(tree[rootIdx])
    else:
        # create the current node, and then find its children
        currNode = Node(tree[rootIdx])
        currNode.children[0] = assembleTree(tree[:rootIdx])
        currNode.children[1] = assembleTree(tree[rootIdx + 1:])

        return currNode

# print reverse in-order traversal with some tabs to print the tree turned sideways for answer verification
def printTree(node, tabs):
    # null check
    if node == None:
        return
    
    # This isn't proper in or
    printTree(node.children[1], tabs + 1)
    print(tabs * '    ' + f'{node.value: 2d}')
    printTree(node.children[0], tabs + 1)
    

# The runner of this problem
if __name__ == "__main__":
    
    tree = [x for x in range(63)]
    print("The array to be treeified: {}\n".format(tree))

    print("Printing of the new Tree")
    printTree(assembleTree(tree), 0)

