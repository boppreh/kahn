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
    a = Kahn(lambda: 4)
    b = Kahn(lambda: 5)
    sum = Kahn(lambda x, y: x + y)
    log = Kahn(print)
    
    # Connect the outputs to inputs.
    # Note that "sum" has two inputs, so it's linked twice.
    connect((a, sum), (b, sum), (sum, log))
    
    # Invoke the processes in order. This step could be done
    # in parallel.
    a()
    b()
    sum()
    log()

