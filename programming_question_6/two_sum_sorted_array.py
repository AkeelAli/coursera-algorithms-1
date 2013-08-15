def binary_search(arr, start, end, num):
    size = (end-start) + 1

    if (size == 2):
        if (arr[start] == num):
            return start
        elif (arr[end] == num):
            return  end
        else:
            return -1
    elif (size == 1): #start == end
        if (arr[start] == num):
            return start
        else:
            return -1

    mid = size/2 + start

    if (num == arr[mid]):
        return mid
    elif num < arr[mid]:
        return binary_search(arr, start, mid - 1, num)
    else:
        return binary_search(arr, mid + 1, end, num)
    
    
def binary_search_lower_index_bound(arr, start, end, num):
    size = (end-start) + 1

    if (size <= 2):
        return start

    mid = size/2 + start

    if (num == arr[mid]):
        return mid
    elif num < arr[mid]:
        return binary_search_lower_index_bound(arr, start, mid - 1, num)
    else:
        return binary_search_lower_index_bound(arr, mid + 1, end, num)

def binary_search_upper_index_bound(arr, start, end, num):
    size = (end-start) + 1

    if (size <= 2):
        return end

    mid = size/2 + start

    if (num == arr[mid]):
        return mid
    elif num < arr[mid]:
        return binary_search_upper_index_bound(arr, start, mid - 1, num)
    else:
        return binary_search_upper_index_bound(arr, mid + 1, end, num)


int_a = []
int_h = {}

#Read sorted integers into hash
f = open("sorted_integers.txt", 'r')

lines = f.readlines()

for line in lines:
    integer = int(line)
    
    if integer not in int_h:
        int_h[integer] = 1
        int_a.append(integer)

f.close()



size = len(int_a)
targets_success = {}
success_target = 0

lower_target_bound = -10000
upper_target_bound = 10000
positive_int_start = 499875


#print int_a

for i in range(0, size):
    x = int_a[i]
    
    if x > 0:
        break

    y_lower = lower_target_bound - x
    y_upper = upper_target_bound - x

    j_start = binary_search_lower_index_bound(int_a, positive_int_start, size - 1, y_lower)
    j_end = binary_search_upper_index_bound(int_a, positive_int_start, size - 1, y_upper)
    
#    print "for x=%d with y=[%d,%d], we found lower index %d & upper index %d" % (x, y_lower, y_upper, j_start, j_end)

    for j in range(j_start, j_end + 1):
        y = int_a[j]
        
        summ = x + y

        if (summ >= lower_target_bound) or (summ <= upper_target_bound):
            targets_success[summ] = 1
        elif (summ > upper_target_bound):
            break

for i in range(lower_target_bound, upper_target_bound + 1):
    if i in targets_success:
        success_target +=1
#        print "SUCCESS: target = %d" % i

print "total %d" % success_target
