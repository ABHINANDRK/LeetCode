# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotateMatrix(matrix):
    start = 0
    end = len(matrix) - 1

    while start < end:
        matrix[start],matrix[end] = matrix[end],matrix[start]
        start += 1
        end -= 1
    
    for i in range(len(matrix)):
        for j in range(i):
            print('i =' + str(i) + ', j =' + str(j))
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)

    


if __name__ == '__main__':
    rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])