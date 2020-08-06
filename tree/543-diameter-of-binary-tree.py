"""
543. 二叉树的直径
https://leetcode-cn.com/problems/diameter-of-binary-tree/
时间 O(N) 遍历每一个节点
空间 O(height)
"""


class Solution:
    ans = 0

    def get_d(self, root):

        def depth(root):
            if not root:
                return -1
            depth_l = depth(root.left) + 1
            depth_r = depth(root.right) + 1
            self.ans = max(self.ans, depth_l + depth_r)
            return max(depth_l, depth_r)

        depth(root)
        return self.ans


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(1)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6

    res = Solution().get_d(t1)
    print(res)
