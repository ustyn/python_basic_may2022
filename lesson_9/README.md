# Lesson 9. Home task.

1. Update git repository with `git pull`
2. You need to implement functions described in `home_task.py`
3. Create your version of the home task : `<your_last_name>.py` in `/lesson_9` folder
4. You will need `users.json` from `/lesson_7` folder for functions `is_admin()` and `write_user_to_file()` 
5. You will need `products.json` from `/lesson_9` folder for function `find_product`.
6. Use examples of code we already have in our repo to read json-file.
7. When ready to publish something (even partial ready) - push to your own branch:
    * create your own branch with command `git checkout -b <your_last_name>`
    * commit `<your_last_name>.py` with some message, if not ready yet - say it in the message
    * push your changes, let me know to get quick response
8. You may found something usefull in `helper.py`

## Hints

You may find very usefull such method of strings:

```python
>>> long_string = "Lorem ipsum dolor si amet ..."
>>> word = "ipsum"
>>> word in long_string
True 
```
Operator `in` for strings returns True if the substring is present in longer string.

This means that you may use it for searching among products' title or description with a given keyword.

But be noticed, that `in` works very strict and matches only exact case-sensitive substrings .

```python
>>> long_string = "Lorem ipsum dolor si amet ..."
>>> word2 = "lorem"
word2 in long_string
False
```