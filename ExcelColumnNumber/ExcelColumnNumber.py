# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# Input: columnTitle = "AB"
# Output: 28
dict = dict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12), ('M', 13), ('N', 14), ('O', 15), ('P', 16), ('Q', 17), ('R', 18), ('S', 19), ('T', 20), ('U', 21), ('V', 22), ('W', 23), ('X', 24), ('Y', 25), ('Z', 26)])

def columnNumber(columnTitle):

    count = 0
    length = len(columnTitle)
    i = 0
    
    while(length > 0):
        stepCount = pow(26, length - 1) * dict[columnTitle[i]]
        count = count + stepCount
        
        i = i + 1
        length = length - 1

    return count

if __name__ == '__main__':
    # print(columnNumber("Z"))