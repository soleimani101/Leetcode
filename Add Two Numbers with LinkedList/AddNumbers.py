# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            # Get the values of the current nodes or 0 if the lists have ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry for the current digits
            total_sum = val1 + val2 + carry
            carry = total_sum // 10  # Integer division gives the carry
            current.next = ListNode(total_sum % 10)  # Remainder gives the new node value

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        # Check if there's any remaining carry
        if carry:
            current.next = ListNode(carry)

        # Return the result, skipping the dummy node
        return dummy.next










# Test cases
solution = Solution()

# Helper function to create linked lists from lists
def createLinkedList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert linked lists to lists
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example 1
nums1 = [2, 4, 3]
nums2 = [5, 6, 4]
l1 = createLinkedList(nums1)
l2 = createLinkedList(nums2)
result = solution.addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [7, 0, 8]

# Example 2
nums1 = [0]
nums2 = [0]
l1 = createLinkedList(nums1)
l2 = createLinkedList(nums2)
result = solution.addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [0]

# Example 3
nums1 = [9, 9, 9, 9, 9, 9, 9]
nums2 = [9, 9, 9, 9]
l1 = createLinkedList(nums1)
l2 = createLinkedList(nums2)
result = solution.addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
