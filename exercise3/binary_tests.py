import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):  # Testing binary searching with no slicing
    def setUp(self) -> None:
        self.testlist = [0, 1, 2, 8, 12, 15]

    def test_binary_search(self):
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 0))
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 1))
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 2))
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 8))
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 12))  # Testing whole
        self.assertTrue(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 15))  # list
        self.assertFalse(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 3))
        self.assertFalse(binary_search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 23))
