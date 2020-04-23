def fibo(n):
    # Recibe un número entero mayor a cero n, y devuelve el elemento n-ésimo de la serie de Fibonacci
    if n <= 2:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

def fiblist(n):
	if n == 1 :
		return [ 1 ]
	else :
		return fiblist(n-1)+[ fibo (n) ]