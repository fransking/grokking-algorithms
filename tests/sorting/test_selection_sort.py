from grokking_algorithms.sorting import selection_sort


def test_selection_sort_on_empty_list():
    items = []
    selection_sort(items)
    assert items == []


def test_selection_sort_on_1_item_list():
    items = [5]
    selection_sort(items)
    assert items == [5]


def test_selection_sort_on_list():
    items = [1, 0, 2, 5, -5, 3]
    selection_sort(items)
    assert items == [-5, 0, 1, 2, 3, 5]
    