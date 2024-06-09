def isListContainsDuplicateNumber(list):
    if len(list) == 0:
        return False

    hashMap = {}

    for i in list:
       if i in hashMap:
           return True
       else:
           hashMap[i] = True
    return False

    
if __name__ == '__main__':
    print(isListContainsDuplicateNumber([1,2,3,1]))