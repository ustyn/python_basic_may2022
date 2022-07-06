# Hello, < class 'Student' >!

This is lesson 10 about classes.

Watch our `classes.py` file and find out how actually `class` creates classes in python. 

```python
class User:
    def __init__(self, first_name, last_name, info=None):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
```

## About self
`self` is not a reserved word, it's just an agreement in python community.
You may name the first argument as you wish, but better don't do it. 

`self` is commonly used name in python, so other developers that will discover your code may be very curious why you name it another way.  

`self` (or whatever first argument) in class methods is a link to an exact instance of this class.

Read [this](https://pyneng.readthedocs.io/ru/latest/book/22_oop_basics/parameter_self.html) article for better understanding of `self`.

## About @staticmethod
But if your method doesn't operate with an instance , for example perform some related functionality , that doesn't need an instance and its attributes - then you may convert your method to a static one.

@staticmethod decorator explanation: [read this](https://medium.com/nuances-of-programming/python-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0-%D0%B8-%D1%8D%D0%BA%D0%B7%D0%B5%D0%BC%D0%BF%D0%BB%D1%8F%D1%80%D0%B0-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0-3e8529d24786).

## About _ _ magic _ _ methods

"Magic" - all methods of the class, that startswith "_ _ " and ends with "_ _", for example 
```__init__()``` or `__str()__`.

Read this [good article](https://habr.com/ru/post/186608/).
