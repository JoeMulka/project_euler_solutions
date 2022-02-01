# Consecutive Prime Sum
import sympy
target_primes = list(sympy.primerange(0,1000000))
num_target_primes = len(target_primes)

this_sum = 0
sums = set()
max_sum = 0
biggest_prime_series = []
longest_length = 0
longest_prime_series = []


for window_size in range(500,600):
    # make a sliding window of increasing size
    left_bound = 0
    right_bound = 0 + window_size
    test_prime_series = target_primes[left_bound:right_bound]
    print("Window size: {}".format(window_size))
    if(not(sum(test_prime_series) > 1000000)):
        while(right_bound <= num_target_primes):
            prime_series = target_primes[left_bound:right_bound]
            this_sum = sum(prime_series)
            if(this_sum < 1000000):
                if len(prime_series) > longest_length:
                    if(sympy.isprime(this_sum)):
                        longest_prime_series = prime_series
                        longest_length = len(prime_series)
            left_bound += 1
            right_bound += 1

print(sum(longest_prime_series))
