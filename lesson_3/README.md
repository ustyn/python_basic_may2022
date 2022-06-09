# LESSON 3
## List comprehension
The syntax of the list comrehension looks like:
`[<expression> for <item> in <iterable> | if <condition>]`

List comprehension may perform or may not perform operation with element (just taking element as is without conversions).

List comprehension may contain or may not contain additional condition.

Watch and try some examples:
1. Get odd numbers from some collection 

 ( comprehension with some condition) 
```python
# some range from 10 to 100 with step 5
all_numbers = range(10, 100, 5)  

# get only odd numbers from previous range
odd_numbers = [i for i in all_numbers if i % 2 != 0]
```
2. Create the list of squares from some collection

 ( comprehension with some operation with every element) 
```python
squares = [item**2 for item in range(20)]
```

3. Print elements from collection without using for loop
   
(for example, print all methods that we can perform with <**list**>, except 'magic' methods )
```python
_ = [print(method) for method in dir(list) if not method.startswith('__')]
```


## Ternary operator
To make one line readable conditions.

`var = true_val if condition else false_val`

Examples. 

Copy and try to see how it works with different values. 

```python
is_after_12 = True      # change to False and watch result
print(f'Now is {"PM" if is_after_12 else "AM"} time.')
```

```python
user_ids = [1, 2, 3]      # change to empty list
message = f'Total {len(user_ids)} users in the list.' if user_ids else 'No users.'
print(message)
```

## Home Task hints
* Copy two `.py` files to a folder `lesson_3`. You need to import and use hardcoded values from `helper.py`.
* Try to run `collections_lesson.py` and watch AssertionError.
* The line like `assert condition , message` checks the condition and if it is False , raises an Error with message. Assertions are widely used in tests.
* Your task is to fix two cases marked **Fixme:**, and make the file run up to the end without Assertion or other errors
* DO NOT correct assertions, correct the code to make Assertions valid.

NOTE: Max points for this task is 90 and absolutely normal and OK.
To get + 10 points more, create the correct cities list without None in a single line.
Yes, actions **# 3** and **# 4** may be completed in a single line, do it to get +10 points.
Your correct result will be a list (or set) with values :
`'Kings Landing', 'Braavos', 'Dragon Stone', 'Winterfell', 'Casterly Rock'`. 
