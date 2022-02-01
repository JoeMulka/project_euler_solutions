# Lychrel numbers
from prob4 import isPalindrome

target_numbers = range(0,10000)
not_lychrel = set()
starting_depth = 51

def reverseNum(to_reverse):
    reversed = int(str(to_reverse)[::-1])
    return(reversed)


for number in target_numbers:
    # A Lychrel number could be processed infinitely, so limit the depth on first pass
    current_iter = number
    for i in range(0,starting_depth):
        # Original ordering doesn't count
        current_iter  = current_iter + reverseNum(current_iter)
        if(isPalindrome(current_iter)):
            not_lychrel.add(number)
            break

print("Found {} non-Lychrel numbers".format(len(not_lychrel)))
print("There are {} candidates for Lychrel numbers".format(len(target_numbers) - len(not_lychrel)))
print("These candidates are: {}".format(set(target_numbers).difference(not_lychrel)))