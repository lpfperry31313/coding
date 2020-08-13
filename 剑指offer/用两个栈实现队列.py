"""
时间 O(1)
空间 O(n)
"""


class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, number):
        self.stack_in.append(number)

    def pop(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else -1


def test_queue():
    q = Queue()
    res = list()
    res.append(q.pop())
    q.push(1)
    q.push(2)
    res.append(q.pop())
    q.push(3)
    res.append(q.pop())
    res.append(q.pop())
    res.append(q.pop())

    assert res == [-1, 1, 2, 3, -1]


if __name__ == '__main__':
    test_queue()
