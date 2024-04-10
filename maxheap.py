class MaxHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        """Adds an element to the maxheap"""

        self._heap.append(entry)

        # Upheap the new value
        self._upheap(index=-1)  # todo

    def _upheap(self, index):
        """Recursively moves the element at the given index up"""

        pass

    def remove(self):
        """Replaces the max element with the 'lowest, right-most' element and upheaps"""

        pass

    def length(self):
        """Gets a count of how many elements are in the heap"""

        return len(self._heap)

    def _downheap(self):
        """Recursively moves the element at the given index down"""

        pass
