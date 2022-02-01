# Powerful Digit Sum
import numpy

def sumDigits(num):
    running_sum = 0
    as_string = str(num)
    for char in as_string:
        running_sum += int(char)
    return(running_sum)


digit_sums = numpy.zeros((100,100))
# There is a 100 x 100 matrix of possible values
for a in range(0,100):
    for b in range(0,100):
        digit_sums[a,b] = sumDigits(a**b)

print("Max digit sum is: {}".format(numpy.amax(digit_sums)))