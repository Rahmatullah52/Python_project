def is_prime(n):
    first = True
    for i in range(2, int(n**0.5)+1):
    # for n in range(2, n%2):
        if n % i == 0:
            first = False
            break
    return first


prime_count = 0  
last_prime_number = 0

for i in range(1,1000001):
     if is_prime(i):
         last_prime_number = i
         prime_count = prime_count +1
        #  print(i)

print("")
print("we have",prime_count,"prime number")
print("last prime number was",last_prime_number)


