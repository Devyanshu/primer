# Queues
##### By [Uma Gunturi](https://github.com/UmaGunturi)

A queue is a linear collection of objects that are inserted and deleted based on the first-in-first-out (FIFO) principle i.e, the elements are always added at the back and removal happens from the beginning.

For Example, if we have a line of people waiting for a bus, the person at the front would enter the bus first.

#### Queues have two opeartions:
 - Enqueue, inserting at the back->Overflow occurs if the queue is full
 - Dequeue, removing from the front->Underflow occurs if the queue is empty
 
#### Queues can be implemented using different data structures.
 - Arrays
 - LinkedList
 
#### How Stack is different from queue?
The difference between stacks and queues is in removing. In a stack we remove the most recently added element but in a queue, we remove the least recently added item.

#### Psuedocode for implementation using arrays
```
enqueue(data) 
    if queue is full ->   
        return 'Overflow'
    else ->
        rear = rear + 1
        queue[rear] <- data

dequeue(data)
    if queue is empty ->
        return 'Underflow'
    else ->
        data = queue[front]
        front <- front + 1
```

#### Further reads
- [GeeksforGeeks](https://www.geeksforgeeks.org/queue-data-structure/)
- [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
