# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

def ransomeNoteCheck(ransomNote, magazine):

    hashTable = {}
    i = 0

    while i < len(magazine):
        if magazine[i] in hashTable:
            hashTable[magazine[i]] = hashTable[magazine[i]] + 1
        else:
            hashTable[magazine[i]] = 1
        i = i + 1
    
    print(hashTable)

    i = 0 
    while i < len(ransomNote):
        if ransomNote[i] in hashTable and hashTable[ransomNote[i]] != 0:
            hashTable[ransomNote[i]] = hashTable[ransomNote[i]] - 1
            i = i + 1
        else:
            return False
    return True

if __name__ == '__main__':
    print(ransomeNoteCheck("a","ba"))