### Problem #1413. Minimum Value to Get Positive Step-by-Step Sum

# Time Complexity: O(n)
# Space Complexity: O(1)

In order to efficiently solve this problem, finding the minimum start value step by step was essential. The chosen value must be sufficient to ensure that the total remains above zero when consuming the input array elements. If it ever falls below zero, then that start value is invalid. Therefore, a larger number had to be selected to guarantee that the total always stays above 0. To determine this number, considering the worst-case scenario of having input elements consisting of negatives like [-100, -100, -100] (assuming the values of an element are between -100 and 100 inclusive) was critical. In such a case, choosing a start value capable of keeping the total above 0 in these input elements became crucial – leading to selecting a number equaling 100 * n (length of the input array) + 1. It's important to note that adding +1 is necessary because it needs to remain above zero.
To find the minimum valid start value as described in code below
