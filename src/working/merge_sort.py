"""Merge sort data structure."""


def mergesort(data):
    try:
        if len(data) > 1:
            half = len(data)//2
            left = data[:half]
            right = data[half:]

            mergesort(left)
            mergesort(right)

            di = 0
            li = 0
            ri = 0

            while len(left) > li and len(right) > ri:
                if left[li] < right[ri]:
                    data[di] = left[li]
                    li += 1
                else:
                    data[di] = right[ri]
                    ri += 1
                di += 1

            while len(left) > li:
                data[di] = left[li]
                li += 1
                di += 1

            while len(right) > ri:
                data[di] = right[ri]
                ri += 1
                di += 1

        # return data

    except TypeError:
        return 'This sort method only accepts values of one type in a list.'


data = [33, 5, 66, 77, 43, 343, 3434, 53, 2, 1, 45, 6]
mergesort(data)
print(data)


# if __name__ == '__main__':  # pragma: no cover
#     from timeit import Timer
#     best = Timer(
#         'mergesort([x for x in range(100)])',
#         "from __main__ import mergesort"
#     )
#     worst = Timer(
#         'mergesort([x for x in range(100)][::-1])',
#         "from __main__ import mergesort; from random import randint"
#     )
#     random = Timer(
#         'mergesort([randint(0, 1000) for x in range(100)][::-1])',
#         "from __main__ import mergesort; from random import randint"
#     )
#     print("""
# Merge sort is a simple sorting algorithm that repeatedly steps through
# the list to be sorted, compares each pair of adjacent items and swaps
# them if they are in the wrong order.
# """)
#     print("#================= best case search 10000x ==============#")
#     print(best.timeit(number=1000))
#     print('')
#     print("#================= worse case search 10000x==============#")
#     print(worst.timeit(number=1000))
#     print('')
#     print("#================= random case search 10000x=============#")
#     print(worst.timeit(number=1000))
#     print('')
