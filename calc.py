# def add (x,y):
#     return x + y

# def sub (x,y):
#     return x - y



primes = [num for num in range(2, 51) if all(num % div != 0 for div in range(2, int(num ** 0.5) + 1))]
print(primes)
