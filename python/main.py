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
        if self.is_full():
            raise IndexError("Hash table is full")
        index = self._hash(key)
        element = self._vector[index]
        while element is not None and element != -1:
            index = (index + 1) % self._vector_size
            element = self._vector[index]
        self._vector[index] = value
        self._quantity_of_inserted_items += 1

    def search(self, key: int, value: int):
        index = self._hash(key)
        element = self._vector[index]
        while element is not None:
            if element == value:
                return index
            index = (index + 1) % self._vector_size
            element = self._vector[index]

    def remove(self, key: int, value: int):
        index = self._hash(key)
        element = self._vector[index]
        while element is not None:
            if element == value:
                self._vector[index] = -1
                self._quantity_of_inserted_items -= 1
                break
            index = (index + 1) % self._vector_size
            element = self._vector[index]

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

    # should collide with 21 and insert on the next position
    hash_table.insert(7, "peter")  # 21 % 7 = 0
    assert hash_table._vector[2] == "peter"

    assert hash_table._quantity_of_inserted_items == 4

    assert not hash_table.is_full()

    hash_table.insert(4, "lucca")
    assert hash_table.is_full()

    assert hash_table.search(15, "james") == 1
    assert hash_table.search(17, "ellen") == 3
    assert hash_table.search(21, "bill") == 0
    assert hash_table.search(7, "peter") == 2

    hash_table.remove(15, "james")
    assert hash_table._vector[1] == -1

    hash_table.remove(7, "peter")
    assert hash_table._vector[2] == -1

    hash_table.insert(12, "john")
    hash_table.insert(8, "poppy")

    try:
        hash_table.insert(8, "poppy")
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, IndexError)

    hash_table.show()
