# Generators
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
Generators in Python are a way to lazy load any iterator, this means that an item is produced only when it's needed. Functions in Python return the whole iterator at once, whereas generators can provide the result one by one, like a stream. Its structure is same as a functions but what makes it a generator is the special keyword ```yield```. The main difference between ```return``` and ```yield``` is that as soon as ```return``` is encountered, the fucntion returns the whole iterator and the control is shifted to the line after the function call, but in ```yield```,  the function returns an item of the iterator and then pauses, it resumes when its called again/consumed in a for-loop. A return statement can also be used in a generator when the control need not return to the generator again.
```
# generator to produce even numbers till 'n'
def generator_demo(n):
    for i in range(0, n, 2):
        # print(i)
        yield i
        
print(generator_demo(10)) # will return generator object

for i in generator_demo(10):
    print(i) # prints even numbers till 10
```

  To prove that the number are yielded one by one and not at once, uncomment the print statement in the generator and run again. You'll see each number getting printed twice, one from the genrator and the other from the for loop.
  
  ## Further reads
- [Generators](https://www.learnpython.org/en/Generators)
- [Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
