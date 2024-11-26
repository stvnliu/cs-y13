def fact(n: int): return n * fact(n-1) if n != 0 else 1

def print_fib(a, b, l):
    print(a)
    print(b)
    print_next_fib(a, b, l-3)

def print_next_fib(a: int, b: int, l: int):
    if l == 0: 
        print(a+b)
        return
    print(a+b)
    return print_next_fib(b, a+b, l-1)

for i in range(1, 10):
    print(fact(i))
print_fib(1, 1, 10)