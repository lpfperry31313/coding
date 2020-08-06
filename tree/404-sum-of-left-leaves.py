"""
404. 左叶子之和
https://leetcode-cn.com/problems/sum-of-left-leaves/
假设树上一共N个节点
时间 O(N)
    遍历每一个节点
空间 O(N)
    最坏情况 退化成链表 O(N)
"""


def solution(root):
    if not root:
        return 0
    if root.left and not root.left.right and not root.left.left:
        return root.left.val + solution(root.right)
    return solution(root.left) + solution(root.right)
