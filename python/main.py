class HashTable:
    _vector: list
    _vector_size: int
    _quantity_limit_of_items: int
    _quantity_of_inserted_items: int = 0

    def __init__(self, vector_size: int):
        self._vector = [None for _ in range(vector_size)]
        self._vector_size = vector_size
        self._quantity_limit_of_items = vector_size // 1.3  # 70% -> load factor

    def _hash(self, key: int):
        # must always return an int between 0 and vector size - 1
        return key % self._vector_size

    def is_full(self):
        return self._quantity_of_inserted_items == self._quantity_limit_of_items

    def insert(self, key: int, value: str):
        index = self._hash(key)
        self._vector[index] = value
        self._quantity_of_inserted_items += 1

    def search(self, key: int):
        index = self._hash(key)
        return self._vector[index]

    def remove(self, key: int):
        index = self._hash(key)
        self._vector[index] = -1  # available
        self._quantity_of_inserted_items -= 1

    def show(self):
        for index, element in enumerate(self._vector):
            print(index, end=": ")
            if element == -1:
                print("-> available")
            elif element is None:
                print("-> empty")
            else:
                print(element)


if __name__ == "__main__":
    # hash table with a size of 7
    hash_table = HashTable(7)

    hash_table.insert(15, "james")  # 15 % 7 = 1
    assert hash_table._vector[1] == "james"

    hash_table.insert(17, "ellen")  # 17 % 17 = 3
    assert hash_table._vector[3] == "ellen"

    hash_table.insert(21, "bill")  # 21 % 7 = 0
    assert hash_table._vector[0] == "bill"

    assert hash_table._quantity_of_inserted_items == 3

    assert not hash_table.is_full()

    hash_table.insert(2, "susan")
    hash_table.insert(4, "lucca")
    assert hash_table.is_full()

    assert hash_table.search(15) == "james"
    assert hash_table.search(17) == "ellen"
    assert hash_table.search(21) == "bill"

    hash_table.remove(15)
    assert hash_table._vector[1] == -1

    hash_table.remove(7)
    assert hash_table._vector[0] == -1

    hash_table.show()
