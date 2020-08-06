"""
101. 对称二叉树
https://leetcode-cn.com/problems/symmetric-tree/
假设树上一共n个节点
时间 O（n）
    遍历每一个节点
空间 O（n）
    1 递归法，空间复杂度和递归层数有关，不超过O（n）
    2 队列法，队列中不会超过n个节点，  不超过O（n）
"""
from collections import deque


def solution_1(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    q = deque()
    q.append(root.left)
    q.append(root.right)
    while q:
        left = q.popleft()
        right = q.popleft()
        if not left and not right:
            continue
        if (not left and right) or (not right and left):
            return False
        if left.val != right.val:
            return False
        q.append(left.left)
        q.append(right.right)
        q.append(left.right)
        q.append(right.left)
    return True


def solution_2(root):
    if not root:
        return True
    return _dfs(root.left, root.right)


def _dfs(left, right):
    if not left and not right:
        return True
    if (not left and right) or (not right and left):
        return False
    if left.val != right.val:
        return False
    return _dfs(left.left, right.right) and _dfs(left.right, right.left)
