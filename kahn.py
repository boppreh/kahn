from collections import deque

class Kahn(object):
    def __init__(self, fn):
        self.fn = fn
        self.in_queues = []
        self.out_queues = []

    def __setitem__(self, index, queue):
        self.out_queues[index] = queue

    def __getitem__(self, index):
        return self.in_queues[index]

    def __call__(self, *inputs):
        if not inputs:
            inputs = [queue.popleft() for queue in self.in_queues]

        results = self.fn(*inputs)

        if isinstance(results, tuple):
            for result, queue in zip(results, self.out_queues):
                queue.append(result)
        elif len(self.out_queues):
            self.out_queues[0].append(results)


def link(producer, consumer):
    if not isinstance(producer, Kahn):
        producer = Kahn(producer)
    if not isinstance(consumer, Kahn):
        consumer = Kahn(consumer)
        
    queue = deque()
    
    producer.out_queues.append(queue)
    consumer.in_queues.append(queue)


def connect(*connections):
    for producer, consumer in connections:

        link(producer, consumer)

if __name__ == '__main__':
    def a():
        return 4
    
    def b(n):
        return n * 2, n
    
    def c(n):
        print(n)
    
    def log(n):
        print('Logged:', n)
    
    connect((a, b), (b, c), (b, log))
    
    ka()
    kb()
    kc()
    klog()
