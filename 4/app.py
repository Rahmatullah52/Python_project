def is_prime(n):
    first = True
    for i in range(2,n):
        if n % i == 0:
            first = False
        return first

print (is_prime(30))            
