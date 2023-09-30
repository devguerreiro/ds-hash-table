import assert from "assert";

class HashTable {
    private vector: (number | string | null)[];
    private vectorSize: number;
    private quantityLimitOfItems: number;
    private quantityOfInsertedItems: number = 0;

    constructor(vectorSize: number) {
        this.vector = Array(vectorSize).fill(null);
        this.vectorSize = vectorSize;
        this.quantityLimitOfItems = Math.floor(vectorSize / 1.3); // 70% -> load factor
    }

    private hash(key: number) {
        return key % this.vectorSize;
    }

    isFull() {
        return this.quantityOfInsertedItems === this.quantityLimitOfItems;
    }

    insert(key: number, value: string) {
        if (this.isFull()) {
            throw new Error("Hash table is full");
        }
        let index = this.hash(key);
        let element = this.vector[index];
        while (element !== null && element !== -1) {
            index = (index + 1) % this.vectorSize;
            element = this.vector[index];
        }
        this.vector[index] = value;
        this.quantityOfInsertedItems++;
    }

    getVector() {
        return this.vector;
    }
}

const hashTable = new HashTable(7);

hashTable.insert(15, "james");
assert.equal(hashTable.getVector()[1], "james");

hashTable.insert(17, "ellen");
assert.equal(hashTable.getVector()[3], "ellen");

hashTable.insert(21, "bill");
assert.equal(hashTable.getVector()[0], "bill");

// should collide with 21 and insert on the next position
hashTable.insert(7, "peter");
assert.equal(hashTable.getVector()[2], "peter");
