from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.currSum = 0
        self.size = size

    def next(self, val: int) -> float:
        # add number to the window
        self.queue.append(val)
        self.currSum += val

        # validate the window
        if len(self.queue) > self.size:
            self.currSum -= self.queue[0]
            self.queue.popleft()

        # calculate the average
        return self.currSum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
