# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

def anagram(s, t):
    if len(s) != len(t):
        return False

    sHashMap = {}
    tHashMap = {}

    for i in range(0, len(s)):
        if(s[i] in sHashMap):
            sHashMap[s[i]] = sHashMap[s[i]] + 1
        else:
            sHashMap[s[i]] = 0

        if(t[i] in tHashMap):
            tHashMap[t[i]] = tHashMap[t[i]] + 1
        else:
            tHashMap[t[i]] = 0

    if(sHashMap == tHashMap):
        return True
    return False
        

if __name__ == "__main__":
    print(anagram("aabb", "aabba"))
