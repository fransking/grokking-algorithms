def selection_sort(items: list):
    if len(items) < 2:
        return items

    # loop over items from start
    for i in range(len(items)):

        # record index of minimum value seen so far starting from i
        min_idx = i

        # from i onwards loop over remainder of the list
        for j in range(i+1, len(items)):

            # update min_idx to point to the minimum value we find when traversing the remainder
            if items[j] < items[min_idx]:
                min_idx = j
        
        # if i and min_idx are now different then swap these items in the list
        if i != min_idx:
            items[i], items[min_idx] = items[min_idx], items[i]

        if __debug__:
            print(items)

    # O(N^2)
