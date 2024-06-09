# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.



def maxSUbArray(nums):
    max = nums[0]
    subArrayCount = nums[0]

    for i in range(1,len(nums)):
        if(subArrayCount + nums[i] < nums[i]):
            subArrayCount = nums[i]
        else:
            subArrayCount = subArrayCount + nums[i]
        
        if(subArrayCount > max):
            max = subArrayCount
    return max
        
  
if __name__ == '__main__':
    print(maxSUbArray([1,2,3,4,5]))