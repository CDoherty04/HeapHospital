class MaxHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        """Adds an element to the maxheap"""

        self._heap.append(entry)

        # Upheap the new value to the parent element
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        """Recursively moves the element at the given index up"""

        if index == 0:
            return

        else:
            # Parent element index
            parent_i = (index-1)//2

            # If the current element is greater than its parent then switch them
            if self._heap[index] > self._heap[parent_i]:
                temp = self._heap[parent_i]
                self._heap[parent_i] = self._heap[index]
                self._heap[index] = temp
                return self._upheap(parent_i)

    def remove(self):
        """Replaces the max element with the 'lowest, right-most' element and upheaps"""

        pass

    def length(self):
        """Gets a count of how many elements are in the heap"""

        return len(self._heap)

    def _downheap(self, index):
        """Recursively moves the element at the given index down"""

        pass
