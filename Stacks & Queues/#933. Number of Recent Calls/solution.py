from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:

        self.requests.append(t)

        # remove expired times
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        #return the number of calls happened within the past 3 seconds
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
