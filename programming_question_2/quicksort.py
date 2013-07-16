comparisons = 0
comp_check = 0


# in-place partition of list A from index l (left) to index r (right)
# using pivot element at index p (pivot)
# return sorted pivot index
def partition(A, l, r, p):
    global comp_check

    # place pivot as first element
    if p != l:
        A[l], A[p] = A[p], A[l]
        p = l
    
    # sweep list from second element to partition
    # index i marks the parition point
    i = l + 1
    for j in range(l+1, r+1):
        comp_check += 1
        if A[j] < A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1

    # place pivot in rightful place
    if p != (i - 1):
        p = i - 1
        A[l], A[p] = A[p], A[l]

    return p

def find_median(l):
    # insertion sort
    for i in range(1, len(l)):
        j = i - 1
        while (j >= 0) and (l[j+1] < l[j]):
            l[j+1], l[j] = l[j], l[j+1]
            j -= 1

    # return median
    mid = len(l) / 2
    #print "Median of "+ str(l) + " is "+ str(l[mid])
    return l[mid]


        

def select_pivot(list, left_idx, right_idx):
    selection = 'median'

    if selection == 'first':
        return left_idx
    elif selection == 'last':
        return right_idx
    elif selection == 'median':
        len = right_idx - left_idx + 1
        if len <= 2:
            return left_idx
        else:
            mid_idx = (right_idx - left_idx)/2 + left_idx
            median = find_median([list[left_idx], list[mid_idx], list[right_idx]])
            return list.index(median)
            


def quicksort(list, left_idx, right_idx):
    global comparisons
    
    length = right_idx - left_idx + 1

    if length <= 1:
        return list

    else:
        pivot_idx = select_pivot(list, left_idx, right_idx)

        comparisons += length - 1
        pivot_idx = partition(list, left_idx, right_idx, pivot_idx)

        # print "After partition around %d: " %list[pivot_idx] + str(list)

        list = quicksort(list, left_idx, pivot_idx - 1)
        list = quicksort(list, pivot_idx + 1, right_idx)

        return list

def test():
    comparisons = 0
    comp_check = 0
    list = [10, 3, 5, 7]
    list = quicksort(list, 0, len(list)-1)
    print list
        
    print comparisons
    print comp_check

def load_integers_into_list(filename):
    l = []

    f = open(filename, 'r')

    for line in f.readlines():
        l.append(int(line))

    f.close()

    return l

if __name__ == "__main__":
    list = load_integers_into_list('QuickSort.txt')

    comparisons = 0
    comp_check = 0
    list = quicksort(list, 0, len(list)-1)

    print comparisons
    print comp_check

