def revString(s):
    i = 0
    j = len(s) - 1

    while i < j:
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        i = i + 1
        j = j - 1
    return s

    
if __name__ == '__main__':
    print(revString(['f','u','n','u','f']))