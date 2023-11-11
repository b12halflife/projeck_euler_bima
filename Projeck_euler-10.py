# menemukan jumlah semua bilangan prima 
def Prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
        else:
            continue
    return prime

primes = (a for a in range(2, 20) if Prime(a))
print(sum(primes))