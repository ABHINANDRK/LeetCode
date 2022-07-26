

# Complexity O(n^2)
def minimumSizeSubarray(target, nums):

    if len(nums) < 1:
        return 0

    left,right = 0,1

    sum = nums[left]

    minLen = len(nums)

    if sum >= target:
        return 1
    

    while(len(nums) > right):            

        if (sum + nums[right]) >= target:
            if ((right - left) + 1) < minLen:
                minLen = (right - left) + 1
            left = left + 1
            right = left + 1
            sum = nums[left] 

            if sum >= target:
                return 1
            
        else:
            sum = sum + nums[right]
            right = right + 1
        
        
    if left == 0 and right == len(nums):
        return 0
    else:
        return minLen

    
# Complexity O(n)
def minimumSize(target, nums):
    if len(nums) < 1:
        return 0

    left,sum = 0, 0

    minLen = len(nums) + 1

    for right in range(len(nums)):
        sum = sum + nums[right]

        while sum >= target:
            if minLen > (right - left) + 1:
                minLen = (right - left) + 1
            sum = sum - nums[left]
            left = left + 1


    if minLen == (len(nums) + 1):
        return 0
    else: 
        return minLen 



if __name__ == '__main__':
   print(minimumSize(11,[1,1,1,1,1,1,1,1]))