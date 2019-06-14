# 时间：20190528
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 难度：Easy(0.25)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 迭代思路：重复一定的算法，达到想要的目的。数学上二分法，牛顿法是很好的迭代例子
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev

        # 递归思路：在return处调用自己（尾递归）
        if not head:
            return prev

        curr, head.next = head.next, prev  # 新旧链表的两个方向同时前进
        return self.reverseList(curr, head)


