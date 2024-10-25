numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
divider = 0
for is_prime in numbers[1::]:
    divider = 0
    for i in range(2, is_prime):
        if is_prime % i == 0:
            divider += 1
    if divider == 0:
            primes.append(is_prime)
    elif divider != 0:
        not_primes.append(is_prime)
print(primes,"\n",not_primes,sep="")







