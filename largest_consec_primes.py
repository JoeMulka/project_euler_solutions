import sympy

target_primes = list(sympy.primerange(0,1000000))
num_target_primes = len(target_primes)
sums = set()
biggest_sum = 0
biggest_prime_series = []

for window_size in range(0,num_target_primes):
    # make a sliding window of increasing size
    left_bound = 0
    right_bound = 0 + window_size
    while(right_bound <= num_target_primes):
        this_sum = sum(target_primes[left_bound:right_bound])
        if(this_sum >= 1000000):
            break
        #sums.add(this_sum)
        if(this_sum > biggest_sum):
            biggest_sum = this_sum
            biggest_prime_series = target_primes[left_bound:right_bound]
        left_bound += 1
        right_bound += 1
        

print(biggest_sum)
print(biggest_prime_series)