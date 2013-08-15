def sort(arr1, arr2):
    sorted_arr = []
    
    size1 = len(arr1)
    size2 = len(arr2)
    size = size1+ size2

    i = 0
    j = 0

    for k in range(0, size):
        if i == size1:
            sorted_arr.append(arr2[j])
            j += 1

        elif j == size2:
            sorted_arr.append(arr1[i])
            i += 1

        elif arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    return sorted_arr


def mergesort(arr):
    size = len(arr)

    if (size <= 1):
        return arr

    mid = size/2

    arr1 = arr[0:mid] # 0 to mid-1
    arr2 = arr[mid:size] # mid to size - 1

    arr1 = mergesort(arr1)
    arr2 = mergesort(arr2)

    print "merge done for arr len %d" % size

    return sort(arr1, arr2)
    



#hash: key = integer, result = occurrence
int_h = {}
#array of distinct integers
int_a = []

#Read integers into hash
f = open("integers.txt", 'r')

lines = f.readlines()

for line in lines:
    integer = int(line)
    
    if integer not in int_h:
        int_h[integer] = 1
        int_a.append(integer)

f.close()


int_a = mergesort(int_a)
size = len(int_a)

#insertion sort array
#print "size: %d" % size
#print "Sorting..."
#for i in range(1, size):
#    if (i % 1000) == 0:
#        print " sorted upto %d" %i
#    for j in range(i - 1, -1, -1):
#        if int_a[j] > int_a[i]:
#            #swap
#            int_a[i], int_a[j] = int_a[j], int_a[i]
#            i -= 1




#Print Sorted integers
f = open("sorted_integers.txt", 'w')

for i in range(0, size):
    f.write(str(int_a[i])+ "\n")

f.close()


success_target = 0

finished_target = False
for target in range(-10000,10001):
    print "target = %d" % target
    for i in range(0, size):
        x = int_a[i]

        if x > 0:
            break

        complement = target - x

        for j in range(size - 1, i, -1):
            y = int_a[j]

            if y < complement:
                break
            
            if ((x + y) == target):
                print "SUCCESS: %d" % target
                success_target += 1
                finised_target = True
                break

        if finished_target:
            finished_target = False
            break
            
print " "
print " "
print success_target
