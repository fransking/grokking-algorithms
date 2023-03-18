from grokking_algorithms.sorting import quick_sort


def test_quick_sort_on_empty_list():
    items = []
    quick_sort(items)
    assert items == []


def test_quick_sort_on_1_item_list():
    items = [5]
    quick_sort(items)
    assert items == [5]


def test_quick_sort():
    items = [1, 0, 2, 5, -5, 3]
    quick_sort(items)
    assert items == [-5, 0, 1, 2, 3, 5]


def test_quick_sort_on_sorted_list():
    items = [1, 2, 3, 4, 5, 6]
    quick_sort(items)
    assert items == [1, 2, 3, 4, 5, 6]

def test_quick_sort_on_reverse_sorted_list():
    items = [6, 5, 4, 3, 2, 1]
    quick_sort(items)
    assert items == [1, 2, 3, 4, 5, 6]


def test_quick_sort_on_partially_sorted_list():
    items = [3, 5, 6, 1, 2, 4]
    quick_sort(items)
    assert items == [1, 2, 3, 4, 5, 6]

def test_quick_sort_on_lists_with_duplicates():
    items = [3, 5, 5, 1, 5, 4]
    quick_sort(items)
    assert items == [1, 3, 4, 5, 5, 5]
