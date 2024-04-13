### Problem #1189. Maximum Number of Balloons

# Time Complexity: O(n)

# Space Complexity: O(n)

To efficiently solve this problem, a hash table was used to record the frequency of characters in the input string. Then, a while loop checked the number of "balloon" instances that could be made from the input string. In each cycle, there had to be enough characters in the hash table to form the word “balloon”. If that wasn't true, the while loop exited and returned the ans variable.
