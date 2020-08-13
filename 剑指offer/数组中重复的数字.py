"""
时间 O(n)
空间 O(1)

"""


def solution(nums):
    n_nums = len(nums)
    if n_nums <= 1:
        return -1
    for i in range(n_nums):
        while i != nums[i]:
            swap_num = nums[nums[i]]
            if swap_num == nums[i]:
                return swap_num
            else:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
    return -1


def test_solution():
    t1 = solution([])
    t2 = solution([3, 2, 1, 0])
    t3 = solution([1, 3, 3, 2, 2])

    map_ans = {
        t1: {-1},
        t2: {-1},
        t3: {2, 3}
    }
    for sol, ans in map_ans.items():
        assert sol in ans, 'my answer {}'.format(sol)
    print('pass all')


if __name__ == '__main__':
    test_solution()
