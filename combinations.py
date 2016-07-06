"""
This method was implemented in itertools.

"""

#combinations('ABCD',2) -> 'AB','AC','AD','BC','BD','CD'
def combinations(iterable, r):
    pool = tuple(iterable)                      #('A','B'...'D')
    n = len(pool)
    if r > n :
        return
    indices = list(range(r))                      
    yield tuple(pool[i] for i in indices)        # first result like : 'AB'
    while True:
        for i in reversed(range(r)):                   
            if indices[i] != i + n -r:
                break
        else :
            return
        indices[i] += 1                                # control the element. [0,1] ->[0,2] ...[0,5] or [0,5] ->[1,5] 
        for j in ( i+1 , r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
