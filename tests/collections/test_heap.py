from grokking_algorithms.collections import Heap

def test_add_items():
    heap = Heap()

    heap.insert(3)
    assert heap._items == [3]

    heap.insert(7)
    assert heap._items == [7, 3]

    heap.insert(4)
    assert heap._items == [7, 3, 4]

    heap.insert(2)
    assert heap._items == [7, 3, 4, 2]

    heap.insert(6)
    assert heap._items == [7, 6, 4, 2, 3]
