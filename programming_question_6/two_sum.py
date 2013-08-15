#hash: key = integer, result = occurrence
int_h = {}

#Read integers into hash
print "Building integer hash..."
f = open("integers.txt", 'r')

lines = f.readlines()

minimum = 0 
maximum = 0

for line in lines:
    integer = int(line)
#    if integer in int_h:
#        int_h[integer] += 1
#    else:
    int_h[integer] = 1

    if integer < minimum:
        minimum = integer
    if integer > maximum:
        maximum = integer

f.close()
print "Finished building integer hash"

print "minimum %d" % minimum
print "maximum %d" % maximum

#two_sum on each target number
for target in range(-10000,10001):
    print "Processing target %d" % target
    for integer in int_h:
        #calculate complement to achieve target
        complement = target - integer

        #ensure distinctness
        if complement == integer:
            continue

        #if the complement exists, then print the target 
        #and move on to the next one
        if complement in int_h:
            print target
            break


