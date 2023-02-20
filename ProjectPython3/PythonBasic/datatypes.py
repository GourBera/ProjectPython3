Collections
    namedtuple( )
    deque
    ChainMap
    Counter
    OrderedDict
    defaultdict

Itertools
    count(start=0, step=1): Returns an infinite iterator that generates an arithmetic progression starting from start and incrementing by step for each iteration.
    cycle(iterable): Returns an infinite iterator that repeats the values in iterable indefinitely.
    repeat(elem, n=None): Returns an iterator that repeats the value elem n times, or indefinitely if n is not provided.
    chain(*iterables): Returns a single iterator that combines multiple iterables into a single sequence.
    groupby(iterable, key=None): Returns an iterator that groups the elements of iterable based on the value returned by key.
    islice(iterable, start, stop, step=1): Returns an iterator that returns a slice of the elements in iterable starting from start and up to but not including stop, with a step size of step.
    starmap(function, iterable): Returns an iterator that applies function to each element of iterable as a tuple.
    tee(iterable, n=2): Returns n independent iterators that each return the elements of iterable.
    zip_longest(*iterables, fillvalue=None): Returns an iterator that aggregates the elements of iterables into tuples, filling in missing values with fillvalue.


