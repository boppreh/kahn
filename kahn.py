from collections import deque

class Kahn(object):
    def __init__(self, fn, n_in, n_out):
        self.fn = fn
        self.n_in = n_in
        self.n_out = n_out
        self.in_queues = [deque() for i in range(self.n_in)]
        self.out_queues = [None for i in range(self.n_out)]

    def __setitem__(self, index, queue):
        self.out_queues[index] = queue

    def __getitem__(self, index):
        return self.in_queues[index]

    def __call__(self):
        inputs = [queue.popleft() for queue in self.in_queues]
        results = self.fn(*inputs) or []
        for result, queue in zip(results, self.out_queues):
            queue.append(result)


def a():
    return (4,)

def b(n):
    print(n)

ka = Kahn(a, 0, 1)
kb = Kahn(b, 1, 0)

ka[0] = kb[0]
ka()
kb()
