### Problem #346. Moving Average from Data Stream

# Time Complexity: O(n)
# Space Complexity: O(n)

To effectively tackle this problem, I utilized the deque data structure, which enabled efficient removal of integers from the beginning of the array, especially as the window size exceeded its intended limit. Upon receiving an input value, I promptly added it to the queue. Subsequently, I verified the validity of the window; if found to be invalid—determined by the window's length surpassing its designated size—I employed an if statement to eliminate values from the start of the deque. Once the window was deemed valid, I proceeded to calculate the average of the numbers within the current window. To track the sum of the input values in the current window, I maintained a currSum variable, updating it as new elements were introduced to the deque. The final step involved returning the average of the numbers in the current window, thus providing a straightforward solution to the problem.
