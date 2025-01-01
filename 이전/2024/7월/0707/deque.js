class Deque {
    constructor() {
        this.items = {};
        this.front = 0;
        this.back = 0;
    }

    // Add an element to the front of the deque
    addFront(element) {
        if (this.isEmpty()) {
            this.addBack(element);
        } else if (this.front > 0) {
            this.front--;
            this.items[this.front] = element;
        } else {
            // Shift all elements to the right
            for (let i = this.back; i > 0; i--) {
                this.items[i] = this.items[i - 1];
            }
            this.back++;
            this.items[0] = element;
        }
    }

    // Add an element to the back of the deque
    addBack(element) {
        this.items[this.back] = element;
        this.back++;
    }

    // Remove an element from the front of the deque
    removeFront() {
        if (this.isEmpty()) {
            return undefined;
        }

        const result = this.items[this.front];
        delete this.items[this.front];
        this.front++;
        if (this.front === this.back) {
            this.front = 0;
            this.back = 0;
        }
        return result;
    }

    // Remove an element from the back of the deque
    removeBack() {
        if (this.isEmpty()) {
            return undefined;
        }

        this.back--;
        const result = this.items[this.back];
        delete this.items[this.back];
        if (this.front === this.back) {
            this.front = 0;
            this.back = 0;
        }
        return result;
    }

    // Check if the deque is empty
    isEmpty() {
        return this.front === this.back;
    }

    // Get the size of the deque
    size() {
        return this.back - this.front;
    }

    // Peek the front element of the deque
    peekFront() {
        if (this.isEmpty()) {
            return undefined;
        }
        return this.items[this.front];
    }

    // Peek the back element of the deque
    peekBack() {
        if (this.isEmpty()) {
            return undefined;
        }
        return this.items[this.back - 1];
    }
}

// Example usage
// const deque = new Deque();
// deque.addBack(1);
// deque.addBack(2);
// deque.addFront(0);
// console.log(deque.peekFront()); // 0
// console.log(deque.peekBack());  // 2
// console.log(deque.removeFront()); // 0
// console.log(deque.removeBack());  // 2
// console.log(deque.size());       // 1



class QueueUsingArray {
    constructor() {
        this.items = [];
    }

    enqueue(element) {
        this.items.push(element);
    }

    dequeue() {
        return this.items.shift();
    }

    size() {
        return this.items.length;
    }

    isEmpty() {
        return this.items.length === 0;
    }
}

// Example usage
// const queueArray = new QueueUsingArray();
// queueArray.enqueue(1);
// queueArray.enqueue(2);
// console.log(queueArray.dequeue()); // 1
// console.log(queueArray.dequeue()); // 2


// const deque = new Deque();
// deque.addBack(1);
// deque.addBack(2);
// console.log(deque.removeFront()); // 1
// console.log(deque.removeFront()); // 2


// Performance test

const iterations = 100000;
const queueArray = new QueueUsingArray();
const deque = new Deque();

// Test Array-based queue
console.time('QueueUsingArray');
for (let i = 0; i < iterations; i++) {
    queueArray.enqueue(i);
}
for (let i = 0; i < iterations; i++) {
    queueArray.dequeue();
}
console.timeEnd('QueueUsingArray');

// Test Deque-based queue
console.time('Deque');
for (let i = 0; i < iterations; i++) {
    deque.addBack(i);
}
for (let i = 0; i < iterations; i++) {
    deque.removeFront();
}
console.timeEnd('Deque');
