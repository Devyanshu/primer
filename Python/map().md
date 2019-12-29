# map()
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
  map() in Python is used to apply a given function to the items of a given iterable or iterables and return a map object.


  map() accepts only one function and atleast one iterable. The number of iterables should be equal to the number of arguments accepted by the passed function. Any iterable such as string, lists, tuples and sets can be passed to the map function. map() returns a map object which can be converted to a list, tuple or a set.
  
  When more than one iterable is given, corresponding elements from each iterable is supplied to the function. If the length of iterables are not same, map() will produce the output with the length equal to that of the smallest iterable and other elements will be ignored.
  
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
  ```
  X = [1, 2, 3, 4]
  Y = [10, 20]
  result = list(map(lambda x,y: x+y, X, Y))
  print(result)
  # prints [11, 22]
  # 3 and 4 from X will be ignored
  # because there corresponding element does not exist in Y
  ```

  #### Further reads
  - [Python map()](https://www.programiz.com/python-programming/methods/built-in/map)
  - [Python docs](https://docs.python.org/3.3/library/functions.html#map)
