### Problem #20. Valid Parentheses

# Time Complexity: O(n)
# Space Complexity: O(n)

To efficiently solve this problem, I utilized a combination of a stack array and a hash table, with the hash table having a fixed size. The process begins by iterating over the input string. If the current character is an open bracket, it is pushed onto the stack. Otherwise, I check whether the top element of the stack corresponds to the current character's counterpart in the hash table. If there's a match, I proceed to the next character in the input string. If there isn't, or if the stack is empty when encountering a closing bracket (indicating the absence of its corresponding open bracket), the function immediately returns false. This is crucial because an unmatched closing bracket suggests an imbalance. After completing the string scan, a final check is performed to ensure the stack is empty. An empty stack indicates all brackets have been properly closed and matched, allowing the function to return true. Otherwise, it returns false, signaling that some brackets have not been properly closed.
