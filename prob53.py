# Combinatoric Selections

# This is probably easiest to solve using Pascal's triangle
# The row number in the triangle is N and the column is R in nCr
# So for nCr for all R for 1 <= n <= 100, we just generate the first 100 rows of the triangle
# It's zero indexed so technically the first 101 rows

def pascalThreshold(num_rows,threshold):
    # The number of entries over the threshold
    counter = 0
    # The tip of the triangle
    prev_row = [1]
    for row in range(1,num_rows+1):
        # The width of the triangle at this row is equal to the row number + 1
        # The edges are always 1, so initialize with 1s and overwrite the middle values
        this_row = [1] * (row + 1)
        for column in range(1,row):
            new_val = prev_row[column-1] + prev_row[column]
            this_row[column] = new_val
            if(new_val > threshold):
                counter += 1
        prev_row = this_row
    return(counter)

test_rows = 100
test_thresh = 1000000

count = pascalThreshold(test_rows,test_thresh)

print("There are {} numbers greater than {} in {} rows of Pascal's triangle".format(count, test_thresh, test_rows))
