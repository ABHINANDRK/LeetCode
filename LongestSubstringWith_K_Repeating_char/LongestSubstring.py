def longestSubstring(s, k):
    if len(s) < 1 :
        return 0

    dict = {}

    left = 0
    longestSubString = 0
    isValid = False

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for right in range(len(s)):
        if dict[s[right]] < k:
            if(right - left) > longestSubString:
                longestSubString = right - left
            left = right
        else:
            longestSubString = right - left + 1
            isValid = True
    
    if isValid:
        return longestSubString
    else:
        return 0





if __name__ == '__main__':
    print(longestSubstring("ababacb",3))
