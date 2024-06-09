# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

     
 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def sort(num1, m, num2, n):
    while m > 0 and n > 0:
        if num1[m - 1] <= num2[n - 1]:
            num1[m + n - 1] = num2[n - 1]
            n = n - 1
        else:
            num1[m + n - 1] = num1[m - 1]
            m = m -1 

    if n > 0:
            num1[:n] = num2[:n]
    print(num1)
    return num1



if __name__ == '__main__':
    sort([10,200,300,0,0,0],3,[20,50,60],3)