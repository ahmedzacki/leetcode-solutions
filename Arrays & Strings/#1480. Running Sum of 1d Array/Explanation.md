### Problem #1480. Running Sum of 1d Array

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I utilized the prefix sum technique. I avoided using an additional array to compute the prefix sum and instead performed it on-the-fly in each iteration of the for loop. By iterating over the input elements with a for loop and starting from the second element (as there is no need to compute prefix sum at the first element), I could simply add the current value to the prefix sum at each iteration of the loop, finding the prefix by obtaining the previous number before the current element. Afterward, I returned the nums array.
