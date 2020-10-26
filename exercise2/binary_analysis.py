import time
import random

"""
Exercise 2 (Online book)
This code compares the two speeds of a recursive binary sort and an iterative binary sort.
Run main to view a simple test and comparison of the speeds, both use the same list.
Something to note is the recursive function will take up a lot more space,
as it will be called to the stack frames many times. Thup to a list of 20k items though we
end up with similar run times. 
Feel free to play around with the list size in main!
"""


def recursivebinarySearch(alist, item):  # Book provided binary search
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursivebinarySearch(alist[:midpoint], item)
            else:
                return recursivebinarySearch(alist[midpoint + 1:], item)


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1


def random_sorted_list(num, start=1, end=100000):
    alist = []
    tmp = random.randint(start, end)

    for x in range(num):

        while tmp in alist:
            tmp = random.randint(start, end)

        alist.append(tmp)

    alist.sort()

    return alist


def recursion_time(alist, search_index):
    start = time.time()
    recursivebinarySearch(alist, alist[search_index])
    time.sleep(0.00000001)
    stop = time.time()
    return f"Recursive search on index {search_index} took {stop - start}"


def iterative_time(alist, search_index):
    start = time.time()
    binarySearch(alist, alist[search_index])
    time.sleep(0.00000001)
    stop = time.time()
    return f"Iterative search on index {search_index} took {stop - start}"


def main():
    search_list = random_sorted_list(20000)  # sorted list of x amount of items
    print(recursion_time(search_list, 0))  # Speed for first item
    print(recursion_time(search_list, len(search_list) // 2))  # Speed for middle item
    print(recursion_time(search_list, len(search_list) - 1))  # Speed for last item
    print()
    print(iterative_time(search_list, 0))  # First item
    print(iterative_time(search_list, len(search_list) // 2))  # Middle item
    print(iterative_time(search_list, len(search_list) - 1))  # Last item


if __name__ == '__main__':
    main()
