from math import floor


def default_partition(items, lo, hi):
    # choose pivot point in the middle
    pivot = items[floor((hi - lo) / 2) + lo]

    # left index
    i = lo - 1

    # right index
    j = hi + 1

    while True:

        # increment the left index until we reach a value that is > pivot
        while True:
            i = i + 1

            if items[i] >= pivot:
                break

        # decrement the right index until we reach a value that is < pivot
        while True:
            j = j - 1
            
            if items[j] <= pivot:
                break

        # if we crossed then return pivot point
        if i >= j:
            return j

        # swap these values
        items[i], items[j] = items[j], items[i]



def quick_sort(items: list, partition_scheme=default_partition):
    if len(items) < 2:
        return items

    _quick_sort(items, 0, len(items) - 1, partition_scheme)


def _quick_sort(items, lo, hi, partition_scheme):
    if lo < hi:
        
        # partition
        partition = partition_scheme(items, lo, hi)
        
        # sort left
        _quick_sort(items, lo, partition, partition_scheme)

        # sort right
        _quick_sort(items, partition + 1, hi, partition_scheme)


        if __debug__:
            print(f'Left: {items[: partition]}')
            print(f'Partition: {items[partition]}')
            print(f'Right: {items[partition+1:]}')
            print('')
