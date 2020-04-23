"""
   Módulo Fibonacci
   2020-04-22
   Greencore - PY0220
   Módulo de ejemplo con la serie de Fibonacci implementada de múltiples maneras.
"""

def fibo(n):
    lst = [0, 1]
    if n <= 2:
        return [1]
    for i in range(2, n+1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst

"""
   fibo(1) -> 1
   fibo(2) -> 1
   fibo(3) -> fibo(2)+fibo(1) -> 1+1 -> 2
   fibo(4) -> fibo(3)+fibo(2) -> (fibo(2)+fibo(1))+1 -> (1+1)+1 -> 3
   fibo(5) -> fibo(4)+fibo(3) -> (fibo(3)+fibo(2))+(fibo(2)+fibo(1)) -> ((fibo(2)+fibo(1))+1)... -> 5
"""