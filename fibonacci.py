def isfibonacci(n):
    if n < 0:
        return False

    a = 0; b = 1
    while n > a:
        a, b = b, b + a
    
    return (n == a or n == b)
    

n = int(input('Enter number: '))

print(f'Is {n} a Fibonacci number? {isfibonacci(n)}')
