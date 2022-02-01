# Permuted Multiples

target_integers = range(100000,200000)

def findSixMult(target_integer):
    highest_mult = 0
    for integer in target_integers:
        digits = sorted(str(integer))
        for multiplier in range(1,7):
            product = integer * multiplier
            product_str = sorted(str(product))
            if(product_str != digits):
                break
            if(multiplier > highest_mult):
                highest_mult = multiplier
            if(multiplier == 6):
                print("found: {}".format(integer))
                return(integer)
    print("highest mult was: {}".format(highest_mult))


found_int = findSixMult(target_integers)
for multiplier in range(1,7):
    print("{} multiple: {}".format(multiplier,(found_int * multiplier)))
    
