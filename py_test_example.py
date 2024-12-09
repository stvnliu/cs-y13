def x(n: int):
    if ( n == 0 ) or ( n == 1 ):
        print(n, end="")
        return
    x(n // 2)
    print(n % 2, end="")
x(255)
