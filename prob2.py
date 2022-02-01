sum = 0
previous = 1
second_previous = 1
current = 0 

while(current < 4000000):
    current = previous + second_previous
    if(current % 2 == 0):
        sum += current
    second_previous = previous
    previous = current

print(sum)