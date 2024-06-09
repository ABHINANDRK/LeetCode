# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


def countBits(value):
    ans = []
    for i in range(0,value):
        ans.append(getBinary(i))
    return ans


def getBinary(value):

    if value == 0:
        return 0

    temp = value
    ans = 0

    while(temp >= 1):
        devisor = temp / 2
        result = temp % 2
        ans = ans + result
        temp = devisor

    return ans

if __name__ == '__main__':
    print(countBits(6))

