# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Input: s = "abc", t = "ahbgdc"
# Output: true

def isSubsequence(s, t):

    j = 0

    for i in range(0,len(s)):
        for p in range(j,len(t)):
            if(s[i] == t[j]){
                j = p + 1
            }




if __name__ = '__main__':

