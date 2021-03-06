"""
itertools.product(*iterables, repeat=1)
  Cartesian product of input iterables.

  Equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

  The nested loops cycle like an odometer with the rightmost element advancing on every iteration. This pattern creates a lexicographic
  ordering so that if the input’s iterables are sorted, the product tuples are emitted in sorted order.

  To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument.
  For example, product(A, repeat=4) means the same as product(A, A, A, A).

  This function is equivalent to the following code, except that the actual implementation does not build up intermediate results 
  in memory:
"""

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
