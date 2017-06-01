"""Test for Binary Heap data structure."""
from binheap import BinaryHeap
import pytest


@pytest.fixture
def build_empty_heap():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    return bh


@pytest.fixture
def build_heap_of_one():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(1)
    return bh


@pytest.fixture
def build_heap_of_two():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(6)
    bh.push(2.254)
    return bh


@pytest.fixture
def build_heap_of_five():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(2)
    bh.push(7)
    bh.push(15)
    bh.push(6.5)
    bh.push(27)
    return bh


@pytest.fixture
def build_heap_of_ten():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(2)
    bh.push(7)
    bh.push(15)
    bh.push(6)
    bh.push(27)
    bh.push(16)
    bh.push(1.5)
    bh.push(3)
    bh.push(8)
    bh.push(9)
    return bh


def test_bheap_init_empty(build_empty_heap):
    """Init with no arg."""
    assert len(build_empty_heap._list) == 0


def test_bheap_init_tuple_one_val():
    """Init with one-item tuple."""
    b = BinaryHeap((9,))
    assert b._list[0] == 9
    assert len(b._list) == 1


def test_bheap_init_tuple_mult_val():
    """Init with longer tuple."""
    b = BinaryHeap((4, 52, 6, -1))
    assert b._list == [-1, 4, 6, 52]
    assert len(b._list) == 4


def test_bheap_init_list_one_val():
    """Init with one-item list."""
    b = BinaryHeap([9])
    assert b._list[0] == 9
    assert len(b._list) == 1


def test_bheap_init_list_mult_val():
    """Init with longer list."""
    b = BinaryHeap([6, 12, -4, 25])
    assert b._list == [-4, 12, 6, 25]
    assert len(b._list) == 4


def test_bheap_init_list_one_bad_val():
    """Init with longer list and one bad val."""
    with pytest.raises(ValueError):
        BinaryHeap([6, 8, 'cake', 25])


# def test_bheap_init_list_one_bad_val_len():
#     """Init with longer list and one bad val."""
#     b = BinaryHeap([6, 8, 'cake', 25])
#     assert b._list == [6, 8]


def test_bheap_push_string(build_empty_heap):
    """Test error on pushing string."""
    with pytest.raises(ValueError):
        build_empty_heap.push('cake')


def test_bheap_push_none(build_empty_heap):
    """Test error on pushing None."""
    with pytest.raises(ValueError):
        build_empty_heap.push(None)


def test_bheap_push_dict(build_empty_heap):
    """Test error on pushing dicts."""
    with pytest.raises(ValueError):
        build_empty_heap.push({'1': 2})


def test_bheap_push_bool(build_empty_heap):
    """Test error on pushing bool."""
    with pytest.raises(ValueError):
        build_empty_heap.push(True)


def test_bheap_push_one_to_empty(build_empty_heap):
    """Test pushing one valid val."""
    b = build_empty_heap
    b.push(14)
    assert b._list[0] == 14


def test_bheap_push_mult_to_empty(build_empty_heap):
    """Test pushing multiple vals."""
    b = build_empty_heap
    b.push(10)
    b.push(9)
    b.push(15)
    b.push(-2)
    b.push(3)
    b.push(1000)
    assert b._list == [-2, 3, 15, 10, 9, 1000]


def test_bheap_push_one_to_many(build_heap_of_ten):
    """Test pushing one valid val."""
    b = build_heap_of_ten
    b.push(45)
    assert len(b._list) == 11
    assert b._list == [1.5, 3, 2, 6, 9, 16, 15, 7, 8, 27, 45]


def test_bheap_push_mult_to_many(build_heap_of_ten):
    """Test pushing multiple vals."""
    b = build_heap_of_ten
    b.push(1)
    b.push(20)
    b.push(45)
    assert len(b._list) == 13
    assert b._list == [1, 1.5, 2, 6, 3, 16, 15, 7, 8, 27, 9, 20, 45]


def test_bheap_push_val_top(build_heap_of_five):
    """Test pushing lowest val in min heap."""
    build_heap_of_five.push(-0.5)
    assert build_heap_of_five._list == [-0.5, 6.5, 2, 7, 27, 15]


def test_bheap_push_val_end(build_heap_of_five):
    """Test pushing end in min heap."""
    build_heap_of_five.push(30)
    assert build_heap_of_five._list == [2, 6.5, 15, 7, 27, 30]


def test_bheap_push_val_middle(build_heap_of_ten):
    """Test pushing middle val to correct index."""
    build_heap_of_ten.push(5)
    assert build_heap_of_ten._list == [1.5, 3, 2, 6, 5, 16, 15, 7, 8, 27, 9]


def test_bheap_pop_empty_heap(build_empty_heap):
    """Test raised error on pop empty heap."""
    with pytest.raises(IndexError):
        build_empty_heap.pop()


def test_bheap_pop_once_left(build_heap_of_ten):
    """Test pop on value on a left branch."""
    b = build_heap_of_ten
    b.pop()
    assert b._list == [2, 3, 15, 6, 9, 16, 27, 7, 8]


def test_bheap_pop_once_right(build_heap_of_five):
    """Test pop on value on a right branch."""
    build_heap_of_five.pop()
    assert build_heap_of_five._list == [6.5, 7, 15, 27]


# def test_bheap_pop_mult():
#     """Test pop on multiple values."""
#     build_heap_of_five.pop()
#     build_heap_of_five.pop()
#     build_heap_of_five.pop()
#     assert build_heap_of_five._list == []


# def test_bheap_pop_all():
#     """Test pop on all list items."""


# def test_bheap_push_pop():
#     """Test pushing and then popping."""


# def test_bheap_pop_push():
#     """Test popping and pushing."""


# def test_bheap_push_pop():
#     """Test pushing twice and then popping."""


# def test_bheap_pop_push():
#     """Test popping twice and pushing."""


# def test_bheap_pop_push_equal():
#     """Test popping twice and pushing twice."""
