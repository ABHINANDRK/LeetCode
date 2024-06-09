# Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
# Input  : arr[] = {100, 200, 300, 400}, k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole array is 2.

def maxSum(arr, k):

    n = len(arr)

    if n < k :
        return None

    
    maxSum = sum(arr[:k])

    for i in range(1, n - k + 1):
        tempSum = sum(arr[i: (i + k)])

        if tempSum > maxSum: 
            maxSum = tempSum
    print(maxSum)


if __name__ == '__main__':

    maxSum([2,3],4)
