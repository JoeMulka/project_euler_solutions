divisor = 2
#remaining = 600851475143
remaining = 600851475143
factors = []

while remaining > 1:
    while (remaining % divisor == 0):
        remaining = remaining / divisor
        factors.append(divisor)
    divisor += 1

print(max(factors))