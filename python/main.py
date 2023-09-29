class HashTable:
    vector: list
    vector_size: int
    quantity_limit_of_items: int
    quantity_of_inserted_items: int = 0

    def __init__(self, vector_size: int):
        self.vector = [None for _ in range(vector_size)]
        self.vector_size = vector_size
        self.quantity_limit_of_items = vector_size // 1.3  # 70%

    def _hash(self, key: int):
        # must always return an int between 0 and vector_size -1
        return key % self.vector_size

    def push(self, key: int):
        index = self._hash(key)
        if self.vector[index] is None:
            self.vector[index] = key

    def search(self, key: int):
        index = self._hash(key)
        value = self.vector[index]
        return value if key == value else None

    def remove(self, key: int):
        index = self._hash(key)
        if self.vector[index] == key:
            self.vector[index] = -1  # available


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

    hash_table.remove(15)
    assert hash_table.vector[1] == -1

    hash_table.remove(7)
    assert hash_table.vector[0] == 21
