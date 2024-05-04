### Problem #933. Number of Recent Calls

# Time Complexity: O(n)
# Space Complexity: O(n)

To effectively address this challenge, I leveraged Python's deque data structure from the collections module. The objective was to ascertain the count of occurrences (calls or pings) within a specific timeframe—namely, the preceding few seconds. The deque was instrumental in tracking the timestamp of each incoming ping. To determine the frequency of calls within the last 3 seconds, I examined the earliest timestamp recorded at the front of the deque. If this timestamp fell outside the 3-second window, it was removed. This process continued until the oldest timestamp in the deque was within the desired timeframe. Ultimately, the solution was as straightforward as returning the deque's length, providing the total count of recent calls.
