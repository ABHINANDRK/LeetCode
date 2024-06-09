# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

 

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.

def deleteAndEarn(nums):

    hashMap = {}
    points = 0

    for i in nums:
       if hashMap.get(i,None) == None:
           hashMap[i] = 1
       else:
           hashMap[i] = hashMap[i] + 1
    
    while len(nums) > 0:
       
        maxIndex = 0
        for i in range(0, len(nums) - 1):
            if nums[maxIndex] < nums[i + 1]:
                maxIndex = i + 1
        
        if(hashMap[nums[maxIndex]] < hashMap[(nums[maxIndex] - 1)]):
            points = points + nums[maxIndex] - 1

            nums.remove(nums[maxIndex] - 1)
            nums.remove(nums[maxIndex])

            hashMap[nums[maxIndex] - 1] = hashMap[nums[maxIndex] - 1] - 1
            hashMap[nums[maxIndex]] = hashMap[nums[maxIndex]] - 1

            if hashMap[nums[maxIndex] - 2] > 0: 
                nums.remove(nums[maxIndex] - 2)
                hashMap[nums[maxIndex] - 2] = hashMap[nums[maxIndex] - 2 ] - 1

        else:
            points = points + nums[maxIndex]

            nums.remove(nums[maxIndex])
            hashMap[nums[maxIndex]] =  hashMap[nums[maxIndex]] - 1

            if hashMap[nums[maxIndex] - 1] > 0:
                nums.remove(nums[maxIndex] - 1)
                hashMap[nums[maxIndex] - 1] = hashMap[nums[maxIndex] - 1] - 1
    return points

    




if __name__ == '__main__':
    deleteAndEarn([2,3])

