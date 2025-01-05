def fact(n: int): return n * fact(n-1) if n != 0 else 1

def compound(p: float, r: float, y: int) -> float: 
    return p if y == 0 else compound(p*r, r, y-1)

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

def fib_nth(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_nth(n-1) + fib_nth(n-2)

def draw_underline(l: int):
    return '-'*l

def test():
    range_end = 15
    print(f"Printing series of factorials from 1 to {range_end}\n{draw_underline(20)}")
    for i in range(1, range_end):
        print(fact(i), end=", " if i < range_end-1 else "\n")
    fib_until = 15
    print(f"\n\nPrinting fibonacci sequence to {fib_until}\n{draw_underline(20)}")
    print_fib(0, 1, fib_until)
    print(fib_nth(5))
    print(compound(36800*4, 1.06, 10) / (43129-3170*12))
def payback(tuition: int, rate: int, salary: int):
    years = 0
    remaining = tuition * 4

    while remaining > 0:
        remaining -= salary
        years += 1
        remaining *= rate
        print(f"Year {years}: remaining: {remaining}")
    print(years)

if __name__ == "__main__":
    test()
