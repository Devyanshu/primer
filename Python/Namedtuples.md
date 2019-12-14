# Namedtuples
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
  Namedtuples in Python can be seen as an improvement of the built-in tuple data type. Just like tuples, they are immutable and can store objects of different data types. 
  When it comes to accessing the stored value, namedtuples have an advantage over tuples because they can be accessed using field names just like dictionary, whereas tuples can only be accessed using indexes. namedtuples provide better structure to store data as compared to tuples.
  
```
from collections import namedtuple
Student = namedtuple('Student',['grade', 'roll_no'])
stud_1 = Student(9.8,1145) 
print(stud_1.grade, stud_1[0]) # data can be accessed 
# by field names as well as indexes, 9.8 9.8 will be printed
```
namedtuple is usually preferred over an immutable class because of it's memory efficiency. For example, in the above code, the same thing can be implemented using a class.
```
class Student:
    def __init__(self, grade, roll_no):
        this.grade = grade
        this.roll_no = roll_no
        
stud_2 = Student(9.8,1145) 
```
 
 Namedtuples can be used to write better and readable code, it provides a structure to the data and serves as a memory efficient substitute for immutable classes.
  
  ## Further reads
  - [Writing clean Python with Namedtuples](https://dbader.org/blog/writing-clean-python-with-namedtuples)
  - [Namedtuples in Python](https://www.geeksforgeeks.org/namedtuple-in-python)
