"""
111. 二叉树的最小深度
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
假设树上一共N个节点
时间 O(N)
    遍历每一个节点
空间 O(N)
    递归调用 "树的高度" 次
    最坏情况  O(N), 最好情况 O(logN)
"""


def solution(self, root):
    if not root:
        return 0
    return self._helper(root, 1)


def _helper(t, count):
    if not t.left and not t.right:
        return 1
    elif t.left and not t.right:
        count += _helper(t.left, count)
    elif t.right and not t.left:
        count += _helper(t.right, count)
    else:
        count += min(_helper(t.right, count), _helper(t.left, count))

    return count
