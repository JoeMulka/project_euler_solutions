# Prime Digit Replacement
from numpy import Inf
import sympy
import itertools
target_primes = list(sympy.primerange(1,1000000))

def modifyPrime(prime,k):
    # k is number of "asterisks"
    prime_str = str(prime)
    index_combinations = []
    indices = range(0,len(prime_str))
    # permutations can be of length 1 to n
    index_combinations += itertools.combinations(indices,k)
    
    modified_list = []
    for combo in index_combinations:
        this_combo_list = []
        # Iterate over the possible combinations of indices to replace
        for replacement_digit in range(0,10):
        # iterate over the possible digits to replace with
            modified_prime = list(prime_str)
            for index in combo:
                modified_prime[index] = str(replacement_digit)
            # Only append it if its the right number of digits, leading zero numbers don't count
            modified_prime_str = "".join(modified_prime)
            if(modified_prime_str[0] != "0"):
                this_combo_list.append(modified_prime_str)
        modified_list.append(set(this_combo_list))
   
    return(modified_list)


def countPrimeFamily(prime):
    overall_fam_list = []
    fam_sizes = []
    for i in range(1,len(str(prime))):
        for fam_list in modifyPrime(prime,i):
            overall_fam_list.append(fam_list)
    for fam_list in overall_fam_list:
        # Count the primes in the list
        counter = 0
        for element in fam_list:
            if(sympy.isprime(int(element))):
                counter += 1
        if(counter == 8):
            print(fam_list)
            as_ints = [int(x) for x in fam_list]
            smallest_prime = min(as_ints)
            print("smallest prime is: {}".format(smallest_prime))
        fam_sizes.append(counter)
    return(fam_sizes)

#print(countPrimeFamily(120383))


for prime in target_primes:
    fam_counts = countPrimeFamily(prime)
    #print("prime: {} fam_counts: {}".format(prime,fam_counts))
    if(8 in fam_counts):
        print("pattern is: {}".format(prime))
        break
        
        

