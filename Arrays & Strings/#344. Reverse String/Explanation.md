### Problem #344. Reverse String

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I decided to use a two-pointer technique. The goal is to modify the string array in place. So, I defined two variables: left and right. Left was set to 0 and right was set to the index of the last element in the array. Then, in each iteration, I would switch the two elements. Then the loop exits when both the left and right indices become equal. Then we are done.
