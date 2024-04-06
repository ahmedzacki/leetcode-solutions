### Problem #2270. Number of Ways to Split Array

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I employed the prefix sum technique. By using a variable to store the sum of all elements in the original nums array, I was able to divide the array into two sections: left and right. For computing the left section, I used another variable to store all sums before the current index in a loop. This involved iterating through a for loop to calculate the left section by adding each element in the array to it during each iteration. Finally, I computed (rightsection - leftsection), checked if (leftsection) was greater than (rightsection), and incremented my count variable if true; otherwise, I moved on to the next iteration of the loop. The final step involved returning the count variable.
