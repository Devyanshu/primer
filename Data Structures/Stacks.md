# Stacks
  ##### By [Devyanshu](https://github.com/Devyanshu)
  Stacks are linear data structure that follow the Last In, First Out (LIFO) principle. This means that the data inserted at the last will be removed first, this is becauase the data can be inserted and removed from one place only.
  
  For example, Let's assume we have a stack of plates, to add more plates to it, we add it from the top and to remove plates from the stack, we again remove it from the top.
  
  Adding elements to a stack is called push whereas removing elements from it is called pop. To better understand this, consider the following image.
  
  
  <img src='https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png' height=400 width=400 alt='Stacks: From Wikipedia'>
  
  
 #### Stacks have two conditions,
  - Overflow, when the stack is full -> can't preform push
  - underflow, when the stack is empty -> can't perform pop
  
 #### Stacks can be implemented using different data structures.
-   Arrays, Overflow condition occurs when the stack size == array size
-   Dynamic Arrays, No overflow condition because the stack can grow in size just like the dynamic array
-   Linked list, No overflow condition because more nodes can be added when required.

All the above implementations can have underflow

#### Pseudocode for array implementation of Stack
```
Stack {
 stack: array
 max_size: int
 top: int
}

push(value) 
    if top == max_size ->   
        return 'Overflow'
    else ->
        stack[top] = value
        top = top + 1


pop()
    if top == 0 ->
        return 'Underflow'
    else ->
        top = top - 1
        return stack[top]
        
```
  
  ## Further reads
  - [Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
  - [GeeksforGeeks](https://www.geeksforgeeks.org/stack-data-structure/)
