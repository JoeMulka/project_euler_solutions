# Square Root Convergents
from fractions import Fraction
import sys



def recursiveFracGen(limit_count,max_limit):
    if (limit_count > max_limit):
        return(Fraction(1,2))
    else:
        return(Fraction(1,2 + recursiveFracGen(limit_count + 1,max_limit)))

def rootTwoApprox(max_iterations):
    for num_iterations in range(0,max_iterations):
        limit = num_iterations - 1
        root_two_approx = 1 + recursiveFracGen(0,limit)
        yield(root_two_approx)

max_iterations = 1000
sys.setrecursionlimit(max_iterations + 50)
approx_gen = rootTwoApprox(max_iterations)

longer_numerators = 0
for approx_frac in approx_gen:
    if(len(str(approx_frac.numerator)) > len(str(approx_frac.denominator))):
        longer_numerators += 1
    
print("There are {} longer numerators".format(longer_numerators))