class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.start = 0
        self.end = 0
        self.k = k
        self.cnt = 0
        self.q = [None] * k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.cnt += 1
        self.q[self.end] = value
        self.end = (self.end + 1) % self.k
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cnt == 0:
            return False
        self.cnt -= 1
        self.q[self.start] = None
        self.start = (self.start + 1) % self.k
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        ret = self.q[self.start]
        if ret is None:
            return -1
        return ret

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        ret = self.q[(self.end-1)%self.k]
        if ret is None:
            return -1
        return ret

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cnt == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cnt == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()