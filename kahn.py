from threading import Thread
from queue import Queue

class Kahn(Thread):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn
        self.in_queues = []
        self.out_queues = []

    def __setitem__(self, index, q):
        self.out_queues[index] = q

    def __getitem__(self, index):
        return self.in_queues[index]

    def run(self):
        while True:
            inputs = [q.get(True) for q in self.in_queues]

            results = self.fn(*inputs)

            if isinstance(results, tuple):
                for result, q in zip(results, self.out_queues):
                    q.put(result)
            elif len(self.out_queues):
                self.out_queues[0].put(results)


def connect(*connections):
    processes = {}
    for producer, consumer in connections:
        if not producer in processes:
            processes[producer] = Kahn(producer)
        if not consumer in processes:
            processes[consumer] = Kahn(consumer)
        
        q = Queue()
        processes[producer].out_queues.append(q)
        processes[consumer].in_queues.append(q)

    for process in processes.values():
        process.start()


if __name__ == '__main__':
    a = lambda: 4
    b = lambda: 5
    add = lambda x, y: x + y
    
    connect((a, add), (b, add), (add, print))
