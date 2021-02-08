class MinHeap:
    def __init__(self):
        self.heap = []
        self.depth = 0

    def pop(self):        
        # first make sure that the heap can be popped
        if len(self.heap) < 1:
            return ""
        else:
            # pop off the first item
            toReturn = self.heap[0]

            # overwrite the value at the root with the value at the last spot in the array
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop() # just get rid of the last item

            # now we have to bubble down that value at the root
            currIdx = 0
            while True:
                # Get the values of the children, if there are any
                leftIdx = (currIdx * 2 + 1) if (currIdx * 2 + 1) < len(self.heap) - 1 else None
                rightIdx = (currIdx * 2 + 2) if (currIdx * 2 + 2) < len(self.heap) - 1 else None
                leftValue = self.heap[leftIdx] if leftIdx != None else None
                rightValue = self.heap[rightIdx] if rightIdx != None else None

                if leftValue != None and leftValue < self.heap[currIdx]:
                    # swap with the left
                    temp = leftValue
                    self.heap[leftIdx] = self.heap[currIdx]
                    self.heap[currIdx] = temp

                    # update where the bubble down index is
                    currIdx = leftIdx
                elif rightValue != None and rightValue < self.heap[currIdx]:
                    # swap with the left
                    temp = rightValue
                    self.heap[rightIdx] = self.heap[currIdx]
                    self.heap[currIdx] = temp

                    # update where the bubble down index is
                    currIdx = rightIdx
                else:
                    # we dont have to bubble down anymore, and the heap is restored
                    break
            
            # now we can return the value, and the heap should have been changed
            return toReturn

    def insert(self, item):
        # append the item to the end of the heap
        self.heap.append(item)

        # bubble that item up
        done = False
        currIdx = len(self.heap) - 1
        while not done:
            # compare the value that we just added to its parent
            parentIdx = currIdx // 2

            # if this is the root, then there is nothing more we can do
            if parentIdx == currIdx:
                done = True
            else:
                # compare the two values
                currValue = self.heap[currIdx]
                parValue = self.heap[parentIdx]

                if currValue < parValue:
                    # swap those two values
                    temp = currValue
                    self.heap[currIdx] = parValue
                    self.heap[parentIdx] = temp

                    # update the current index to the new index we are looking at
                    currIdx = parentIdx
                else:
                    done = True