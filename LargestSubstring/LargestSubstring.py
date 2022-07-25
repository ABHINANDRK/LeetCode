# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



def largestSubstring(str):
    if len(str) < 1 : 
        return 0
    

    left = 0
    right = 1

    maxSubstringLen = 1

    dict = {}
    dict[str[left]] = left

    while right < len(str):
        
        if((str[right] in dict) and dict[str[right]] >= left):
            dict[str[right]] = right
            left = dict[str[right]] + 1
            
        else:
            dict[str[right]] = right

            if(((right - left) + 1) > maxSubstringLen):
                maxSubstringLen = (right - left) + 1

        
        right = right + 1
        print(dict)

    return maxSubstringLen


if __name__ == '__main__':
    print(largestSubstring("bbbbb"))