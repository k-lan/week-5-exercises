import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.H = HashTable()
        self.H[54] = "cat"
        self.H[26] = "dog"
        self.H[93] = "lion"
        self.H[17] = "tiger"
        self.H[77] = "bird"
        self.H[31] = "cow"
        self.H[44] = "goat"
        self.H[55] = "pig"
        self.H[20] = "chicken"

    def test_contains(self):
        self.assertTrue(self.H.__contains__(54))
        self.assertTrue(self.H.__contains__(20))
        self.assertTrue(self.H.__contains__(17))

        self.assertFalse(self.H.__contains__(1))
        self.assertFalse(self.H.__contains__(100))

    def test_del(self):
        del self.H[54]
        self.assertFalse(self.H.__contains__(54))
        del self.H[20]
        self.assertFalse(self.H.__contains__(20))
        del self.H[1]

    def test_resize(self):
        self.H[23] = "Boy"
        self.H[46] = "Girl"
        self.H[88] = "Mom"
        self.H[90] = "Dad"
        self.assertTrue(self.H.size == 23)