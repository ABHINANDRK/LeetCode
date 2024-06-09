# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


class ArrayMaster:
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def rotateArray(self):
        length = len(self.array)
        if length <= 1:
            return

        rotations = self.k % length


        for i in range(0,rotations):
            temp = None
            for j in range(length - 1,-1,-1):
                if temp == None:
                    temp = self.array[j]
                else:
                    self.array[j + 1] = self.array[j]
            
            self.array[0] = temp

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
            
        
                
            # temp = None




if __name__ == '__main__':
    master = ArrayMaster([1,2,3,4,5,6],0)
    # master.rotateArray()
    # print(master.array)
