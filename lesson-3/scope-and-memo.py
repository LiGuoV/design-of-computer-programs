def memo(f):
    cache = {}
    def _f(*args):
        print(*args,cache)
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(*args)
    return _f
@memo
def fib(n):
    if n<=1:return 1
    else:return fib(n-1)+fib(n-2)

# fib = memo(fib)

@memo
def square(n):
    return n*n


print(fib(4))
print('============')
print(fib(4))