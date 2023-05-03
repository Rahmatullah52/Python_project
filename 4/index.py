def is_prime(n): 

    avval = True
    for n in range(2,i):
        if i % n == 0:
            avval = False
    return avval

prime_count = 0
for i in range(1,1001):
    if is_prime(i):
        prime_count = prime_count +1
        print(i)

print("")
print("We have",prime_count,"prime number")















# B = 13
#
# first = True
# for bad in range(2,B):
#     if B % bad == 0:
#         first =False
#
# if first:
#     print("It's prime")
# else:
#     print("it's npt prime")
