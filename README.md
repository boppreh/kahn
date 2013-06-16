kahn
====

This small library implements a basic Kahn process network system. By wrapping 
functions in Kahn objects, you can link the return of one into the parameters
of another you form the network.

The linked processes can be called, flowing data through the network in a
buffered way (a queue is put between the output and input). This allows the
network to process data by simple pipelining with parallel implementations.


Example
-------

    # Processes.
    a = lambda: 4
    b = lambda n: n * 2, n
    c = lambda n: print(n+1)
    log = lambda n: print("Logged:", n)
    
    # Link the first output of "a" to the first input of "b",
    # the first output of "b" to the first input of "c", and
    # so on. "b" has two outputs, so it's linked to two nodes.
    connect((a, b), (b, c), (b, log))
    
    # Invoke the process "a", pushing its output into the 
    # input buffer of the nextx node.
    ka()
    kb()
    kc()
    klog()
