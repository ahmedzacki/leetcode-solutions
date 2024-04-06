class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Find every substring of length k
        # Counting vowels in each substring and returning maximum number

        # Sliding window technique
        vowels = set('aeiou')

        # Initialize variables
        left = right = curr = ans = 0

        # Build first window with length k while counting vowels
        for i in range(k):
            if s[i] in vowels:
                curr += 1

		# Updating answer
		ans = max(ans ,curr)

		# Building remaining subarrays
  		for right in range(k,len(s)):
    		if s[right]in voweles:
        		curr+= 1
        	if s[left]in voweles:
            	curr-=1
			left+=1
		
	  ans=max(ans ,curr)
  		
	return ans
