# Add Two Numbers
# Medium

# 19759

# 3963

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def getValue(self,head):
        if head.next == None:
            return head.val
        else:
            return self.getValue(head.next) * 10 + head.val

    def addTwoNumbers(self, l1, l2):
         firstNum = self.getValue(l1)
         secondNum = self.getValue(l2)

         return self.createList(firstNum + secondNum)
        
    def createList(self,num):
        head = ListNode(num%10)
        num = num // 10
        tempHead = head

        while(num > 0):
            carry = num % 10
            num = num // 10
            node = ListNode(carry)
            head.next = node
            head = node
               
        return tempHead

            


    def addTwoNumbers(self, l1, l2):
         firstNum = self.getValue(l1)
         secondNum = self.getValue(l2)

         return self.createList(firstNum + secondNum)

       
         
        # print(l2.val)
 



if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node4.next = node5
    node6 = ListNode(4)
    node5.next = node6

    headFirst = node1

    headSecond = node4

    solution = Solution()
    head = solution.addTwoNumbers(headFirst,headSecond)
    print(head.next.next.val)

