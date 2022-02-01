three_mults = []
this_mult = 3
while(this_mult < 1000):
    three_mults.append(this_mult)
    this_mult += 3
five_mults = []
this_mult = 5
while(this_mult < 1000):
    five_mults.append(this_mult)
    this_mult += 5

combined_mults = set(three_mults + five_mults)
mult_sum = sum(combined_mults)
print(mult_sum)