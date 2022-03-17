def factorial(n) :
    if (n == 1):
        return 1
    else:
        return ( 1 / n + factorial(n-1) )
print('%f'%(factorial(5)))