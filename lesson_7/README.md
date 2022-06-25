# FUNCTIONS notes

## *args, **kwargs

```python
def some_function(*args, **kwargs):
    pass
```
`*args` stands for _let's take all arguments that were passed inside function, and we don't know how many arguments it would be_

The type of the `args` will be tuple.

`**kwargs` - the same but for key word arguments

The type of `kwargs` will be dict.

## Mutable as default argument
DO NOT REPEAT
```python
def bad_function(list_to_process=[]):
    # this is a realy bad function with mutable as a default argument
    # may cause unexpected results!!!
    pass
```

Really bad practice, never do it if you really understand what you are doing. 

But better use `None`. Really.

## Recursive function

* Perfect if you use it correctly.
* May become your nightmare otherwise.
* Always remember how to exit the recursion - there should be the condition to enter , and DEFINITELY should be a condition to exit.

Watch examples of recursive functions in `lesson_7.py`

**Hint.** 
Working dir while running `lesson7.py` should be not the `.../python_basic_may2022/lesson_7`
but just `.../python_basic_may2022/`

## os.path

Is extremely helpfull when you work with files / pathes

```python
import os

folder = os.getcwd()
```
`.getcwd() `- returns current working directory

```python
files_and_folders = os.listdir(folder)
```
`.listdir()` - returns all names in the folder, both files and folders


`os.path.isdir(path)` - returns True if the `path` is folder (directory)

`os.path.isfile(path)` - returns True if the `path` is file

`os.path.exists(path)` - returns True if `path` is a correct path, if we can read file/dir 

`os.path.join(names)` - joins `names`  into the correct path (according to operation system separator)

names may be folders, subfolder, filename etc 

`os.path.split(path)`  - returns a tuple of folder and file name

# Read it from git
## Hello from Katya
