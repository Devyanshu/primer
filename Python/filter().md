# filter()
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
  filter() in Python is used to filter out items of an iterable using a given function. The given functions is applied to each item of the iterable, if the return value is true, the item will be part of the output of filter(),  otherwise it is discarded.
  
  
  filter() accepts only one function and one iterable. Any iterable such as string, lists, tuples and sets can be passed. It returns a fiter object which can be converted to a list, tuple or a set.
  
  When ```None``` is given instead of a function, the truth value of each item of the iterable decides whether it passes or not.
  
  #### Examples
  ```
  numbers = [10, 15, 52, 87, 23, 71, 100, 108]
  even_numbers = list(filter(lambda x: x%2==0, numbers))
  print(even_numbers)
  # prints [10, 52, 100, 108]
   ```
   ```
   values = [1, 0, True, None, False, 22]
   result = list(filter(None, values))
   print(result)
   # prints [1, True, 22]
   # only elements with truth value as true will be printed
   ```

  #### Further reads
  - [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter)
  - [Python docs](https://docs.python.org/3.3/library/functions.html#filter)
