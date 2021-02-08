import random
import MinHeap

# I just want to create a tree, and print it out
# maybe just work with array implementation first?
tree = [random.randint(0, 50) for x in range(20)]

# in-order traversal
def inOrderTraversal(tree, index):
    # make sure the index we are trying to access is valid
    if index > len(tree) - 1:
        return
    
    # left, current, right
    inOrderTraversal(tree, (2*index + 1))
    print(tree[index])
    inOrderTraversal(tree, (2*index + 2))

def preOrderTraversal(tree, index):
    if index > len(tree) - 1:
        return
    
    # Root, Left, right
    print(tree[index])
    preOrderTraversal(tree, (2*index + 1))
    preOrderTraversal(tree, (2*index + 2))

def postOrderTraversal(tree, index):
    if index > len(tree) - 1:
        return
    
    # Left, right, Root
    preOrderTraversal(tree, (2*index + 1))
    preOrderTraversal(tree, (2*index + 2))
    print(tree[index])

print("In-Order Traversal")
inOrderTraversal(tree, 0)

print("Pre-Order Traversal")
preOrderTraversal(tree, 0)

print("Post-Order Traversal")
postOrderTraversal(tree, 0)

# lets test the heap stuff that we just made
heap = MinHeap.MinHeap()
for x in range(20):
    heap.insert(random.randint(0, 100))

print("Current Min Heap: {}".format(heap.heap))
