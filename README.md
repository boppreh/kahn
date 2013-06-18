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
    # Declare the processes.
    a = lambda: 4
    b = lambda: 5
    add = lambda x, y: x + y
    
    # Link the processes and start the network.
    connect((a, add), (b, add), (add, print))
