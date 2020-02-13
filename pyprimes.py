# Damien Connolly
# Computing the primes


P = []

for i in range(2, 100):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        P.append(i)

print(P)