import assert, { fail } from "assert";

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

    search(key: number, value: string) {
        let index = this.hash(key);
        let element = this.vector[index];
        while (element !== null) {
            if (element === value) {
                return index;
            }
            index = (index + 1) % this.vectorSize;
            element = this.vector[index];
        }
    }

    remove(key: number, value: string) {
        let index = this.hash(key);
        let element = this.vector[index];
        while (element !== null) {
            if (element === value) {
                this.vector[index] = -1;
                this.quantityOfInsertedItems--;
                break;
            }
            index = (index + 1) % this.vectorSize;
            element = this.vector[index];
        }
    }

    show() {
        this.vector.forEach((element, index) => {
            process.stdout.write(index + ": ");
            if (element === -1) {
                console.log("-> available");
            } else if (element === null) {
                console.log("-> empty");
            } else {
                console.log(element);
            }
        });
    }

    getVector() {
        return this.vector;
    }

    getQuantityOfInsertedItems() {
        return this.quantityOfInsertedItems;
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

assert.equal(hashTable.getQuantityOfInsertedItems(), 4);

assert.equal(hashTable.isFull(), false);

hashTable.insert(4, "lucca");
assert.equal(hashTable.isFull(), true);

assert.equal(hashTable.search(15, "james"), 1);
assert.equal(hashTable.search(17, "ellen"), 3);
assert.equal(hashTable.search(21, "bill"), 0);
assert.equal(hashTable.search(7, "peter"), 2);

hashTable.remove(15, "james");
assert.equal(hashTable.getVector()[1], -1);

hashTable.remove(7, "peter");
assert.equal(hashTable.getVector()[2], -1);

hashTable.insert(12, "john");
hashTable.insert(8, "poppy");

assert.throws(() => hashTable.insert(8, "poppy"));

hashTable.show();
