# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums, target):

    hashMap = {}

    for i in range(0,len(nums)):
        if nums[i] in hashMap:
            if (2 * nums[i]) == target:
                return [hashMap[nums[i]],i]
        else:
            hashMap[nums[i]] = i
    print(hashMap)
    
    for i in nums:
        if ((target - i) in hashMap) and (target - i) != target/2:
            return [hashMap[i],hashMap[target - i]]

    return []


if __name__ == "__main__":
    print(twoSum([3,2,4],6))
