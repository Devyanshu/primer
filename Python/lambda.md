# lambda
##### By [Devyanshu](https://github.com/Devyanshu)

```lambda``` keyword in Python is used to declare anonymous or use-and-throw functions, i.e functions with no name that will be used only once. Though it's not logically wrong to use them more than once, it is rarely used and only when it's intended task is very simple and has use only once or when we have to pass a small function as a parameter in other functions. It is important to note that ```lambda``` functions can only execute one statement and return it's value, thus, writing complex functions using it is both diffcult to read and write and hence it is recommended to use ```def``` instead.

```
lambda x: x**2  #lambda function to calculate square of a number
```

``` 
numbers = [45, 2, 18, 81] 
numbers.sort(key=lambda x: x%5)  # sorts the list according to the remainder given when divided by 5
# gives [45, 81, 2, 18]
```



## Further reads
- [Python lambda](https://www.w3schools.com/python/python_lambda.asp)
- [Anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function)
