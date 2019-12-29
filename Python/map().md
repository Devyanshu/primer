# map()
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
  map() in Python is used to apply a given function to the items of a given iterable or iterables and return a map object.


  map() accepts only one function and atleast one iterable. The number of iterables should be equal to the number of arguments accepted by the passed function. Any iterable such as string, lists, tuples and sets can be passed to the map function. map() rerturns a map object which can be convererted to a list, tuple or a set.
  
  #### Examples
  ```
  names = ['John', 'Alice', 'Bob']
  name_lengths = list(map(lambda x: len(x), names))
  print(name_lengths)
  # prints [4, 5, 3]
  ```
  ```
  number = [2, 3, 4]
  exponent = [10, 4, 2]
  result = list(map(lambda x, y: x**y, number, exponent))
  # calculates x**y, where x is from number and y from exponent
  print(result)
  # prints [1024, 81, 16]
  ```

  #### Further reads
  - [Python map()](https://www.programiz.com/python-programming/methods/built-in/map)
  - [Python docs](https://docs.python.org/3.3/library/functions.html#map)
