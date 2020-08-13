"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8

方法一： (1+n)n/2 - sum(nums) 时间 O(n), 空间 O(1)
方法二： 二分                  时间 O(logn), 空间 O(1)

思路：



       0 1 3
index  0 1 2
       l m r
           lr

        0
index   0
        lr

if nums[i] == i:
    search right
if nums[i] > i:
    search left
if nums[i] < i:
    impossible
"""


class Solution:
    def find_missing(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


def test_find_missing():
    assert Solution().find_missing([0, 1, 3]) == 2
    assert Solution().find_missing([0, 1, 2, 3, 4, 5, 6, 7, 9]) == 8
    assert Solution().find_missing([1]) == 0
    assert Solution().find_missing([0]) == 1


if __name__ == '__main__':
    test_find_missing()
