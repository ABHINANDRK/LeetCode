def search(nums: List[int], target: int) -> int:
        
    start = 0
    end = len(nums) - 1
    mid = 0

    while(start < end):
        mid = ((start + end) // 2)
        print(mid)

        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            start = mid + 1
            else:
                end = mid - 1
        
        if(nums[mid] == target):
            return mid

        return -1

if __name__ == '__main__':
    # print(columnNumber("Z"))