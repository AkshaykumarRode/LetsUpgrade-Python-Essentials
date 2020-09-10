def is_prime(num):
   for j in range(2, num):
      if num % j == 0:
         return False
   else:
      return True
primes = filter(is_prime, range(1, 2500))
print(list(primes))
