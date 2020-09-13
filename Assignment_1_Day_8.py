# Fibonacci series using decorators

def inputf(fun):
    def inp():
        nterms = int(input("Enter the number of terms of fibonacci series:"))
        fun(nterms)
    return inp

def fibo(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
series = inputf(fibo)
series()