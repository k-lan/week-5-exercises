class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        if self.is_full():
            self.resize()

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    #  __________________________________Exercises_________________________________________________

    def __contains__(self, key):
        """
        Solution for exercise 5.
        Takes the key and notifies user if true or false
        """
        contains = False
        if key in self.slots:
            contains = True
        return contains

    def remove_item(self, key):
        """
                Remove a key and its data from the HashTable
                Uses contains method to make sure key is in the table
                """
        if self.__contains__(key):
            hash_value = self.hashfunction(key, len(self.slots))

            if self.slots[hash_value] != key:
                hash_value = self.rehash(key, len(self.slots))
                while self.slots[hash_value] != key:
                    hash_value = self.rehash(hash_value, len(self.slots))

            self.slots[hash_value] = None
            self.data[hash_value] = None

        else:
            print(f"{key} is not in the table")

    def __delitem__(self, key):
        self.remove_item(key)

    def is_full(self):
        is_full = False
        amount_of_items = 0
        for item in self.slots:
            if item != None:
                amount_of_items += 1
        if amount_of_items >= self.size:  # The slots are full
            is_full = True
        return is_full

    def resize(self, new_size=23):
        if is_prime(new_size):
            self.slots = self.slots + ([None] * (new_size - self.size))
            self.data = self.data + ([None] * (new_size - self.size))
            self.size = new_size
        else:
            print("Please enter a prime number")


def is_prime(num):
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
    return is_prime


def main():
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    H[23] = "Boy"
    H[46] = "Girl"
    H[88] = "Mom"
    H[90] = "Dad"
    print(H.slots)
    print(H.data)



if __name__ == '__main__':
    main()
