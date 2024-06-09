# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def searchMatrix(matrix, target):
    noOfRows = len(matrix) 
    noOfColumns = len(matrix[0])

    if target < matrix[0][0] or target > matrix[noOfRows - 1][noOfColumns - 1]:
        return False

    j = noOfRows - 1
    i = 0

    while i <= j:
        middle = (i + j) // 2
        array = matrix[middle]

        if(target >= array[0] and target <= array[noOfColumns -1]):
            return binarySearch(array, target)
        elif target < array[0]:
           j = middle - 1
        elif(target > array[noOfColumns - 1]):
            i = middle + 1
    return False


def binarySearch(array, target):
    i = 0
    j = len(array) - 1

    while(i <= j):
        middle = (i + j)//2
        if array[middle] == target:
            return True
        elif target < array[middle]:
            j = middle - 1
        else:
            i = middle + 1
    return False


if __name__ == '__main__':
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1))
