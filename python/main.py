class HashTable:
    vector: list
    size: int

    def __init__(self, size: int):
        self.vector = [None for _ in range(size)]
        self.size = size

    def _hash(self, key: int):
        # must always return an int between 0 and size -1
        return key % self.size

    def push(self, key: int):
        index = self._hash(key)
        if self.vector[index] is None:
            self.vector[index] = key

    def search(self, key: int):
        index = self._hash(key)
        value = self.vector[index]
        return value if key == value else None


if __name__ == "__main__":
    # hash table with a size of 7
    hash_table = HashTable(7)

    hash_table.push(15)  # 15 % 7 = 1
    assert hash_table.vector[1] == 15

    hash_table.push(17)  # 17 % 17 = 3
    assert hash_table.vector[3] == 17

    hash_table.push(21)  # 21 % 7 = 0
    assert hash_table.vector[0] == 21

    hash_table.push(7)  # 7 % 7 = 0
    assert hash_table.vector[0] == 21

    assert hash_table.search(15) == 15
    assert hash_table.search(17) == 17
    assert hash_table.search(21) == 21
    assert hash_table.search(7) is None
