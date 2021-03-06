class Queue:
    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        return self._queue.append(value)

    # pop() The removed element from the array;undefined if the array is empty.
    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        if (index < 0 and len(self._queue)):
            raise IndexError
        return self._queue[index]
