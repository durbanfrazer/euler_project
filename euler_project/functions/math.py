
def summation(x):
    return x*(x+1)/2
    

''' get the xth fibonacci number'''
_fibonacci_map = {1:1,2:2}
def fibonacci(x):
    if (x not in _fibonacci_map):
        _fibonacci_map[x] = fibonacci(x-1) + fibonacci(x-2)
    return _fibonacci_map[x]
    