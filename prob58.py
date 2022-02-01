# Spiral Primes
import sympy

class Ring:
    def __init__(self, side_length, start_index):
        self.side_length = side_length
        self.start_index = start_index
        self.end_index = side_length**2
    def __str__(self):
        return("Starting Index: {}, Ending Index: {}, Side Length: {}".format(self.start_index,self.end_index,self.side_length))
    def getDiags(self):
        top_right = self.start_index + (self.side_length - 2)
        top_left = top_right + self.side_length - 1
        bottom_left = top_left + self.side_length - 1
        return(top_right,top_left,bottom_left)
    


def getPrimeCount(ring):
    prime_count = 0
    for diag in ring.getDiags():
        if(sympy.isprime(diag)):
            prime_count += 1
    return(prime_count)


prime_ratio = 1.0
starting_index = 2
side_length = 1
max_iter = 20000
iter = 0
total_primes = 0
total_diags = 1
while(prime_ratio > 0.1 and iter < max_iter):
    side_length += 2
    iter += 1
    # Make a ring object to represent this ring of the spiral
    new_ring = Ring(side_length,starting_index)
    # The total number of diags increases by four each iteration
    total_diags += 4
    total_primes += getPrimeCount(new_ring)
    prime_ratio = total_primes / total_diags
    #print("Side length: {}  Prime Ratio: {}".format(side_length,prime_ratio))
    starting_index = new_ring.end_index + 1
    
print("Iterations: {}".format(iter))
print("Last side length: {}".format(side_length))
print("Last prime ratio: {}".format(prime_ratio))
#print([str(x) for x in all_rings])
