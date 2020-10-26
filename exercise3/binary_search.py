"""
Binary Search without any slicing.
Exercise 3 in Runestone book
Run with binary_tests
"""

def binarySearch(alist, item):  # Book provided binary search
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


def binary_search_no_slice(alist, start, last, item):  # A binary search with no slicing or list creation/copying
    if last - start == 1 and last != 1:  # if last == 1 then we're looking at the first item in the list
        return False
    else:
        midpoint = (start + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_no_slice(alist, 0, midpoint, item)
            else:
                return binary_search_no_slice(alist, midpoint, last, item)


def main():
    """
    I would suggest running binary_tests to check the non slicing solution
    """
    testlist2 = [0, 1, 2, 8, 12, 15]
    print(binary_search_no_slice(testlist2, 0, len(testlist2), 9))
    print(binary_search_no_slice(testlist2, 0, len(testlist2), 0))

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))


if __name__ == '__main__':
    main()
